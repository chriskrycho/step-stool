from jinja2 import debug

__author__ = 'Chris Krycho'
__copyright__ = '2013 Chris Krycho'


from os import path, walk
from markdown import Markdown


def generate_site(config):
    '''
    Generate the site:

    - Get the site configuration
    - Get all the content from the content directory
    - Render the content
    '''
    site_config = config['site']
    # source = config['site']['content_source']
    # destination = config['site']['content_output']
    # md_extensions = config['site']['markdown_extensions']
    #
    # for root, dirs, files in walk(source):
    #     converted_files = get_content_and_meta(files, md_extensions)
        # for file in converted_files:
        #     if file.meta.template:
        #         template = file.meta.template
        #     else:
        #         template = config['default_template']


def get_content_and_meta(files, extensions):
    md = Markdown(extensions=extensions, output_format='html5')

    converted_files = {}
    for file in files:
        content = md.convert(file)
        converted_files[file] = {'content': content, 'meta': md.Meta}

    return converted_files
