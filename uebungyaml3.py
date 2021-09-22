import yaml

dict_file = [{'name' : 'Herisau', 'plz' : '9100', 'streets' : ['Kasernenstrasse', 'Bahnhofsstrasse', 'Alpsteinstrasse']},
{'name' : 'Rapperswil', 'plz' : '8640', 'streets' : ['Oberseestrasse', 'Jonastrasse']}]

with open('yaml_file2.yaml', 'w') as file:
    documents = yaml.dump(dict_file, file)