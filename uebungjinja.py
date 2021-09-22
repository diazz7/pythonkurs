from jinja2 import Environment, FileSystemLoader
import yaml

#laod data from YAML into Python dict
yaml_file = open('config.yml')
config_data = yaml.load(yaml_file)

env = Environment(loader=FileSystemLoader('./'), trim_blocks=True,lstrip_blocks=True)
template = env.get_template('template.txt')

print(template.render(config_data))