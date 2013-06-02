__author__ = 'Chris Krycho'
__copyright__ = '2013 Chris Krycho'


from yaml import load


def get_config(document):
    config = load(document)
    return config
