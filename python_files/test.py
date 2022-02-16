import yaml
opt = yaml.load(open('./arg.yml'), Loader=yaml.FullLoader)
print(opt['dataset-path'])