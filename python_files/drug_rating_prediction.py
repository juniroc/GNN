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

import argparse

parser = argparse.ArgumentParser(description='get argument from argparse')
parser.add_argument('--dataset-path', '-dp', type=str, help='dataset path')
parser.add_argument('--train', '-t', type=str, help='dataset path')
parser.add_argument('--pickle-dir', type=str, help='pickle path')


args = parser.parse_args()

class create_graph:
    def __init__(self, tmp_):
        # self.data_path = args.dataset_path
        # self.pickle_dir = args.pickle_dir
        self.data_path = tmp_

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


    def _save_dict(self, dict_lst, dir_path, file_name_lst):

        while len(dict_lst)!=0:
            dict_ = dict_lst.pop(0)
            file_name = file_name_lst.pop(0)
            ### tmp_dir_path : /workspace/22gnn/python_files/datas/v_1
            with open(f'{dir_path}/{file_name}.pickle', 'wb') as handle:
                pickle.dump(dict_, handle, protocol=pickle.HIGHEST_PROTOCOL)


    def get_graph(self):
        
        if args.train=='train':
            
            df_ = self._get_dataset()

            df_ = preprocessing(df_).preprocess()
            
            drug_dict = self._get_dict(df_, 'DrugId')
            patient_feat_dict = self._get_dict(df_, ['Age', 'Sex'])
            cond_dict = self._get_dict(df_, 'Condition')

            drug_side_dict, side_dict, drug_feat_dict = self._get_drug_feat_dict(df_, drug_dict)

            dict_lst = [drug_dict, patient_feat_dict, cond_dict, drug_side_dict, side_dict, drug_feat_dict]
            name_lst = ['drug_dict', 'patient_feat_dict', 'cond_dict', 'drug_side_dict', 'side_dict', 'drug_feat_dict']
            self._save_dict(dict_lst, self.pickle_dir, name_lst)




            ## get node_array
            patient_arr = np.array(df_['patient_id'])

            # mapping using dictionary
            drug_arr = self._get_n_arr(df_, drug_dict, 'DrugId')
            cond_arr = self._get_n_arr(df_, cond_dict, 'Condition')

            ## label_edge_array
            label_arr = torch.tensor(df_['Satisfaction'])

            print(patient_arr)
            print(drug_arr)
            print(cond_arr)

            ### TRAIN data
            hetero_graph_t = dgl.heterograph({
                ('patient', 'satisfaction', 'drug'): (patient_arr_t, drug_arr_t),
                ('condition', 'symptom', 'patient'): (cond_arr_t, patient_arr_t),
                ('drug', 'Easy', 'patient'): (drug_arr_t[df_t['EaseofUse']==1], patient_arr_t[df_t['EaseofUse']==1]),
                ('drug', 'Effectiveness', 'condition'): (drug_arr_t[df_t['Effectiveness']==1], cond_arr_t[df_t['Effectiveness']==1])
                })
            return 




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




if __name__ == '__main__':
    tmp = create_graph('../kaggle_data/webmd.ftr')
    tmp.get_graph()