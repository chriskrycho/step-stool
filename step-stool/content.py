__author__ = ''
__copyright__ = '2013 Chris Krycho'


from markdown import markdownFromFile as md_file


def get_content_and_meta(file):
    meta = md_file()
    content = ''
    return meta, content
