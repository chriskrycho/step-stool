__author__ = 'Chris Krycho'
__copyright__ = '2013 Chris Krycho'


from yaml import load


def get_config(document):
    config = load(document)
    return config

def gen_config():
    ''' Generate a configuration file with default values. '''
    pass
