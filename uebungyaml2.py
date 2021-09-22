import yaml

with open('yaml_file2.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)