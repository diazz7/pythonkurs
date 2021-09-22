import yaml

dict_file = [{'Land' : ['Schweiz', 'USA', 'Deutschland', 'China']},
{'Hauptstadt' : ['Bern', 'Washington', 'Berlin', 'Peking']},{'Tiere' : ['Hund', 'Katze']}]

with open('yaml_file.yaml', 'w') as file:
    documents = yaml.dump(dict_file, file)