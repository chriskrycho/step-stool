__author__ = 'Chris Krycho'
__copyright__ = '2013 Chris Krycho'


from yaml import dump, load


def get_config(yaml_string):
    config = dump(load(yaml_string))
    return config
