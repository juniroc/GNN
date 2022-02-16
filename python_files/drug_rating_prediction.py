import os
import sys
import pandas as pd
import numpy as np
import dgl
import torch
import torch.nn as nn
import torch.nn.functional as F
import itertools
import torchmetrics
import pickle
import model_file

import argparse

parser = argparse.ArgumentParser(description='get argument from argparse')
parser.add_argument('--dataset-path', '-dp', type=str, help='dataset path')
parser.add_argument('--train', '-t', type=str, help='`train` / `inference` set mode ')
parser.add_argument('--version-dir', type=str, help='data version(pickle files) path')
parser.add_argument('--m-ratio', type=float, help='train/val-ratio', default=0.8)
parser.add_argument('--input-f', type=int, help='number of input features', default=10)
parser.add_argument('--hidden-f', type=int, help='number of hidden features', default=20)
parser.add_argument('--output-f', type=int, help='number of output features', default=5)



args = parser.parse_args()

class create_graph:
    def __init__(self):
        self.data_path = args.dataset_path
        self.version_dir = args.version_dir
        self.train = args.train

    def _get_dataset(self):
        _, extension = os.path.splitext(self.data_path)

        data_format = extension[1:]

        if data_format=='csv':
            df = pd.read_csv(self.data_path)

        elif data_format=='ftr':
            df = pd.read_feather(self.data_path)
    
        return df
            
    def _get_dict(self, df, column: any):
        index = 0
        val_lst = [i for i in df[column].value_counts().index]
        
        dictionary = {}
        
        for i in val_lst:
            dictionary[i] = index
            index += 1
        
        return dictionary

    def _get_drug_feat_dict(self, df_, drug_dictionary):
        # drug_side_dict
        drug_side_dict = {}

        ### most frequency side effect of each drug (dictionary)
        for i in drug_dictionary.keys():
            most_side = df_[df_['DrugId']==i]['Sides'].value_counts().index[0]
            drug_side_dict[i] = most_side


        # side_dict (Cause of sides duplicate, using set)
        side_dict = {}
        index = 0
        side_set = set()
        side_set.update(drug_side_dict.values())

        # side effect dictionary
        for j in side_set:
            side_dict[j] = index
            index += 1

        # drug_feat_dict
        drug_feat_dict = {}

        for i in drug_side_dict.keys():
            drug_feat_dict[drug_dictionary[i]] = side_dict[drug_side_dict[i]]

        return drug_side_dict, side_dict, drug_feat_dict


    def _get_n_arr(self, dataframe, dictionary, column):    
        num_lst = [int(dictionary[i]) for i in dataframe[column]]
        
        return np.array(num_lst)


    def _save_dict(self, dictionary, dir_path):
        
        ### tmp_dir_path : /workspace/22gnn/python_files/datas/v_1
        with open(f'{dir_path}/total_dict.pickle', 'wb') as handle:
            pickle.dump(dictionary, handle, protocol=pickle.HIGHEST_PROTOCOL)

        # save to npy file
        for i in dictionary.keys():
            if type(i).__name__=='ndarray':
                np.save(f'{dir_path}/{i}.npy', dictionary[i])

            else:
                with open(f'{dir_path}/{i}.pickle', 'wb') as handle:
                    pickle.dump(dictionary[i], handle, protocol=pickle.HIGHEST_PROTOCOL)

            # elif type(i).__name__=='dict':
            #     with open(f'{dir_path}/{i}.pickle', 'wb') as handle:
            #         pickle.dump(dictionary[i], handle, protocol=pickle.HIGHEST_PROTOCOL)
            
            # elif type(i).__name__=='DGLHeteroGraph':
            #     with open(f'{dir_path}/{i}.pickle', 'wb') as handle:
            #         pickle.dump(dictionary[i], handle, protocol=pickle.HIGHEST_PROTOCOL)

    def _load_dict(self, dir_path):
        with open(f'{dir_path}/total_dict.pickle', 'rb') as f:
            # The protocol version used is detected automatically, so we do not
            # have to specify it.
            dict_ = pickle.load(f)

        return dict_

    # embedding features
    def _get_embed(self, len_keys, lst, embed_n):

        embedding_table = nn.Embedding(num_embeddings=len_keys, 
                                embedding_dim=embed_n)

        
        embed_feat = embedding_table(torch.LongTensor(lst))

        return embed_feat


    def get_graph(self):
        if self.train=='train':
            
            df_ = self._get_dataset()

            df_ = preprocessing(df_).preprocess()
            
            drug_dict = self._get_dict(df_, 'DrugId')
            patient_feat_dict = self._get_dict(df_, ['Age', 'Sex'])
            cond_dict = self._get_dict(df_, 'Condition')

            drug_side_dict, side_dict, drug_feat_dict = self._get_drug_feat_dict(df_, drug_dict)

            train_dict = {'drug_dict':drug_dict, 'patient_feat_dict':patient_feat_dict, 'cond_dict':cond_dict, 'drug_side_dict':drug_side_dict, 'side_dict':side_dict, 'drug_feat_dict':drug_feat_dict}
            
            ## get node_array
            patient_arr = np.array(df_['patient_id'])

            # mapping using dictionary
            drug_arr = self._get_n_arr(df_, drug_dict, 'DrugId')
            cond_arr = self._get_n_arr(df_, cond_dict, 'Condition')

            train_dict.update({'patient_arr':patient_arr, 'drug_arr':drug_arr, 'cond_arr':cond_arr})
            ## label_edge_array
            label_arr = torch.tensor(df_['Satisfaction'])
            train_dict.update({'satisfaction':label_arr})

            ### TRAIN data
            hetero_graph_t = dgl.heterograph({
                ('patient', 'satisfaction', 'drug'): (patient_arr, drug_arr),
                ('condition', 'symptom', 'patient'): (cond_arr, patient_arr),
                ('drug', 'Easy', 'patient'): (drug_arr[df_['EaseofUse']==1], patient_arr[df_['EaseofUse']==1]),
                ('drug', 'Effectiveness', 'condition'): (drug_arr[df_['Effectiveness']==1], cond_arr[df_['Effectiveness']==1])
                })

            ###  Train node feature embedding table
            # patient
            patient_f_lst = [patient_feat_dict[(df_['Age'][i], df_['Sex'][i])] for i in range(len(df_))]
            # patient embedding
            patient_embed = self._get_embed(len(patient_feat_dict.keys()), patient_f_lst, 10)    # ( 280127 * 10 ) -> 22 types

            # condition
            cond_f_lst = [i for i in range(len(cond_dict.values()))]
            # condition embedding
            cond_embed = self._get_embed(len(cond_dict.values()), cond_f_lst, 10)    # ( 1584 * 10 ) -> 1584 Condition types

            # drug
            drug_f_lst = [i for i in drug_feat_dict.values()]
            # drug embedding
            drug_embed = self._get_embed(len(drug_feat_dict.keys()), drug_f_lst, 10)   # ( 4522 * 10 ) -> 4522 drug types and 1557 side effect types
            

            train_dict.update({'patient_embed':patient_embed, 'cond_embed':cond_embed, 'drug_embed':drug_embed})

            # get nodes features and edge label
            hetero_graph_t.edges['satisfaction'].data['label'] = label_arr
            hetero_graph_t.nodes['patient'].data['feature'] = patient_embed
            hetero_graph_t.nodes['drug'].data['feature'] = drug_embed
            hetero_graph_t.nodes['condition'].data['feature'] = cond_embed

            train_dict.update({'hetero_graph_t':hetero_graph_t})

            self._save_dict(train_dict, self.version_dir)

            return hetero_graph_t

        elif self.train=='inference':
            
            df_ = self._get_dataset()

            df_ = preprocessing(df_).preprocess()
            
            # load dictionaries
            total_dict = self._load_dict(self.version_dir)

            ### added_inference array
            patient_arr_inf = np.array(df_['patient_id'])
            try:
                drug_arr_inf = self._get_n_arr(df_, total_dict['drug_dict'], 'DrugId')
            
            except ValueError:
                print('there is no DrugId in dictionary, Try training or Check dictionary some keys')

            try:
                cond_arr_inf = self._get_n_arr(df_, total_dict['cond_dict'], 'Condition')
            
            except ValueError:
                print('there is no Condition in dictionary, Try training or Check dictionary some keys')

            # label concat with train - inference
            label_arr_inf = torch.tensor(list(df_['Satisfaction']))

            label_arr_inf = torch.cat([total_dict['satisfaction'], label_arr_inf], 0)


            ### add nodes and edges
            hetero_graph_inf = dgl.add_edges(total_dict['hetero_graph_t'], patient_arr_inf, drug_arr_inf, etype='satisfaction')
            hetero_graph_inf = dgl.add_edges(hetero_graph_inf, cond_arr_inf, patient_arr_inf, etype='symptom')
            hetero_graph_inf = dgl.add_edges(hetero_graph_inf, drug_arr_inf[df_['EaseofUse']==1], patient_arr_inf[df_['EaseofUse']==1], etype='Easy')
            hetero_graph_inf = dgl.add_edges(hetero_graph_inf, drug_arr_inf[df_['Effectiveness']==1], cond_arr_inf[df_['Effectiveness']==1], etype='Effectiveness')

            # get inference node feature embedding
            patient_embed_inf = total_dict['patient_embed']
            drug_embed_inf = total_dict['drug_embed']
            cond_embed_inf = total_dict['cond_embed']

            hetero_graph_inf.edges['satisfaction'].data['label'] = label_arr_inf
            hetero_graph_inf.nodes['patient'].data['feature'] = patient_embed_inf
            hetero_graph_inf.nodes['drug'].data['feature'] = drug_embed_inf
            hetero_graph_inf.nodes['condition'].data['feature'] = cond_embed_inf


            return hetero_graph_inf, len(df_)

        else:
            print("you should check train or inference")




class preprocessing:
    def __init__(self, df_, ):
        self.df = df_

    def _remove_null_data(self, df_):
        for i in df_.columns:
            df_ = df_[df_[i]!=' ']    # remove ' ' (empty space) value

        df_.dropna(inplace=True)
        df_.reset_index(drop=True, inplace=True)

        return df_

    # change 4~5 to 1, and 0~3 to 0
    def _change_values(self, df_):
        df_['Effectiveness'] = df_['Effectiveness'].apply(lambda x: 0 if (x<4) else 1)
        df_['EaseofUse'] = df_['EaseofUse'].apply(lambda x: 0 if (x<4) else 1)
        df_['Satisfaction'] = df_['Satisfaction'].apply(lambda x: 0 if (x<4) else 1)

        return df_

    def preprocess(self):
        df_ = self._remove_null_data(self.df)
        df_ = self._change_values(df_)

        # get `patient_id` column
        df_['patient_id'] = [i for i in range(len(df_))]

        return df_


class model_:
    def __init__(self):
        
        self.creating_graph = create_graph()
        
        self.mask_ratio = args.m_ratio
        self.input_f = args.input_f
        self.hidden_f = args.hidden_f
        self.output_f = args.output_f
        self.version_dir = args.version_dir
        

    def train(self):
        hetero_graph_t = self.creating_graph.get_graph()

        # edge length
        num_edges = len(hetero_graph_t.edata['label'][('patient', 'satisfaction', 'drug')])

        # train / validation masking
        train_mask = torch.zeros(num_edges, dtype=torch.bool).bernoulli(self.mask_ratio)
        val_mask = ~train_mask

        dec_graph_t = hetero_graph_t['patient', :, 'drug']

        label_arr_t = hetero_graph_t.edges['satisfaction'].data['label']

        model = model_file.Model(self.input_f, self.hidden_f, self.output_f, hetero_graph_t.etypes, True)

        node_features_t = {
            'patient': hetero_graph_t.nodes['patient'].data['feature'],
            'drug':hetero_graph_t.nodes['drug'].data['feature'],
            'condition':hetero_graph_t.nodes['condition'].data['feature']
            }
        
        opt = torch.optim.Adam(model.parameters())

        model.train()
        for epoch in range(300):
            logits = model(hetero_graph_t, node_features_t, dec_graph_t)
            loss = F.cross_entropy(logits[train_mask], label_arr_t[train_mask])
            opt.zero_grad()
            loss.backward(retain_graph=True)
            opt.step()

            if epoch % 5 == 0:
                acc_val = torchmetrics.functional.accuracy(logits[val_mask], label_arr_t[val_mask])
                print(f"--------- {epoch} ---------")
                print('val_acc : ', acc_val)


        torch.save(model, f'{self.version_dir}/model.pth')

    def infer(self):
        hetero_graph_inf, inf_length = self.creating_graph.get_graph()

        dec_graph_inf = hetero_graph_inf['patient', :, 'drug']

        label_arr_inf = hetero_graph_inf.edges['satisfaction'].data['label']

        node_features_inf = {
            'patient': hetero_graph_inf.nodes['patient'].data['feature'],
            'drug':hetero_graph_inf.nodes['drug'].data['feature'],
            'condition':hetero_graph_inf.nodes['condition'].data['feature']
            }

        model = torch.load(f'{self.version_dir}/model.pth')

        model.eval()

        with torch.no_grad():
            test_logit = model(hetero_graph_inf, node_features_inf, dec_graph_inf)
        
        inference_acc = torchmetrics.functional.accuracy(test_logit[inf_length:], label_arr_inf[inf_length:])
        print("acc : ", inference_acc.item())


if __name__ == '__main__':
    test = model_()
    if args.train=='train':
        test.train()
    elif args.train=='inference':
        test.infer()