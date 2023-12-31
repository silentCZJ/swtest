import yaml

def read_yaml(file):
    with open(file,'r',encoding='utf-8') as f:
        config = yaml.load(f,yaml.FullLoader)
        return config