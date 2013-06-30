__author__ = 'Chris Krycho'
__copyright__ = '2013 Chris Krycho'

from logging import error
from os import path, walk
from sys import exit

try:
    from markdown import Markdown
    from mixins import DictAsMember

except ImportError as import_error:
    error(import_error)
    exit()


def convert_source(config):
    '''
    Generate the site:

    - Get the site configuration
    - Get all the content from the content directory
    - Render the content
    '''
    md = Markdown(extensions=config.markdown_extensions, output_format='html5')
    converted = {}
    for root, dirs, file_names in walk(config.site.content.source):
        for file_name in file_names:
            file_path = path.join(root, file_name)
            md_text = open(file_path, 'r').read()
            content = md.convert(md_text)
            converted[file_name] = {'content': content, 'meta': md.Meta}

    return DictAsMember(converted)
