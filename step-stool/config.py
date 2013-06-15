__author__ = 'Chris Krycho'
__copyright__ = 'Copyright © 2013 Chris Krycho'

# System modules
import os.path as path

# Dependency modules
from yaml import load


def configured(directory):
    '''
    Check whether the directory has a configuration file already. If the file
    exists, assume it has been configured.
    '''
    config_file_name = 'config.yaml'
    full_path = path.join(directory, config_file_name)
    if path.exists(full_path):
        return True
    else:
        return False


def get_config(document):
    config = load(document)
    return config


def gen_config():
    ''' Generate a configuration file with default values.
    '''
    pass


def setup():
    pass
