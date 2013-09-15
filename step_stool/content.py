__author__ = 'Chris Krycho'
__copyright__ = '2013 Chris Krycho'

from collections import namedtuple
from datetime import datetime as dt
from logging import error
from os import path, walk
from shutil import copytree, copy, rmtree
import errno
from sys import exit

try:
    from markdown import Markdown
    from mixins import DictAsMember
    import render

except ImportError as import_error:
    error(import_error)
    exit()


Content_Pair = namedtuple('Content_Pair', ['content', 'meta'])
OUTPUT_EXTENSION = '.html'
DATE_FORMAT = '%Y-%m-%d %H:%M'


def copy_required_template_elements(site_config):
    copy_names = site_config.template.copy_elements
    copy_sources = [path.join(site_config.template.directory, copy_name) for copy_name in copy_names]
    copy_destinations = [path.join(site_config.content.destination, copy_name) for copy_name in copy_names]
    copy_pairs = zip(copy_sources, copy_destinations)
    for source, destination in copy_pairs:
        if path.exists(destination):
            rmtree(destination)

        try:
            copytree(source, destination)
        except OSError as exc:
            if exc.errno == errno.ENOTDIR:
                copy(source, destination)
            else:
                raise


def paginate(posts_per_page, documents):
    slices = len(documents) // posts_per_page + 1
    return [documents[n:((n+1)*posts_per_page)] for n in range(slices)]


def write_site(site_config, output):
    '''
    Write all the content in output to files by slug with extension `.html`,
    then copy any necessary files from the template directory (e.g. Javascript
    or CSS) to the output directory.
    '''

    # Iterate over blog, home, categories, tags, etc.
    for element in output:
        if output[element] is not None:
            for slug in output[element]:
                output_path = path.join(site_config.content.destination, slug + OUTPUT_EXTENSION)
                with open(output_path, 'w') as file:
                    file.write(output[element][slug])

    copy_required_template_elements(site_config)


class Builder():
    def __init__(self, config):
        self.config = config
        self.options = self.config.site.options  # Shortcut for easy access to most commonly used elements

        self.renderer = render.Renderer(self.config.site)
        self.posts_per_page = self.options.posts_per_page
        self.ignored = []

    def build_site(self, converted_documents):
        self.documents = converted_documents

        output = {'pages': self.build_pages(),
                  'blog': self.build_blog() if self.options.blog.use else None,
                  'categories': self.build_cats() if self.options.categories.use else None,
                  'tags': self.build_tags() if self.options.tags.use else None}

        output['home'] = self.build_home() if self.options.home.use else output['blog']

        return output

    def build_blog(self):
        posts = [doc for doc in self.documents if doc.meta['type'] == 'post']

        pages = {}
        counter = 0
        for page_set in paginate(self.posts_per_page, posts):
            counter += 1
            pages[str(counter)] = self.renderer.render_page_set(page_set)

        return pages

    def build_cats(self):
        pages = {}
        categories = []
        for doc in self.documents:
            if 'category' in doc.meta:
                for category in doc.meta['category']:
                    categories.append(category) if category not in categories else None
        return pages

    def build_home(self):
        '''
        Generate the index page based on the settings in config. If the site is set
        to use a home page and supplied a home page slug, it will attempt to use a
        file with that slug. If the site is set to use a home page and no home slug
        exists, an error is printed. If the site is not set to use a home page, the
        function returns immediately.
        '''
        if self.options.home.use:
            if self.options.home.slug in self.documents:
                rendered_page = self.renderer.render_page(self.documents[self.options.home.slug])
                return {'index': rendered_page}

            else:
                error_msg = 'Specified slug {} not in list of documents supplied. Could not build home page.'
                error_msg = error_msg.format(self.options.home.slug)
                error(error_msg)

    def build_pages(self):
        '''
        Generate each of the standalone pages. Pages are rendered using a template
        specified in the file's meta, if (1) a template is specified there and (2)
        a template with that name is available. If no template file with that name
        exists, or if none is specified in the meta, the default is used. Note that
        a 'page' is *any* page on the site, not just standalone, non-blog pages.
        '''
        pages = {doc.meta['slug']: self.renderer.render_page(doc) for doc in self.documents}
        return pages


    def build_tags(self):
        tags = []
        for doc in self.documents:
            if 'tags' in doc.meta:
                for tag in doc.meta['tags']:
                    tags.append(tag) if tag not in tags else None

        return None

    def convert_source(self):
        '''
        Convert all Markdown pages to HTML and metadata pairs. Returns a list of
        all the content pairs, sorted by date.
        '''
        md = Markdown(extensions=self.config.markdown_extensions, output_format='html5')
        converted_docs = []
        for root, dirs, file_names in walk(self.config.site.content.source):
            for file_name in file_names:
                file_path = path.join(root, file_name)
                plain_slug, extension = path.splitext(file_name)

                with open(file_path, 'r') as file:
                    md_document = file.read()
                    html_document = md.convert(md_document)
                    converted_doc = Content_Pair(html_document, md.Meta)
                    self.__normalize_meta(converted_doc.meta, plain_slug)
                    converted_docs.append(converted_doc)
                    md.reset()

        converted_docs = [doc for doc in converted_docs if not doc.meta['ignore']]
        converted_docs.sort(key=lambda post: post.meta['sort_date'], reverse=True)
        return converted_docs

    def __normalize_date(self, metadata):
        '''
        At present this simply adds a sort_date field to the metadata. In the
        future, I plan to use the parsedatetime_ tool to convert dates fuzzily so
        users can put in more flexible date formats.

        _parsedatetime: https://github.com/bear/parsedatetime/blob/master/examples/basic.py
        '''
        if metadata['type'] == 'post':
            try:
                metadata['date'] = metadata['date'][0]
                metadata['sort_date'] = dt.strptime(metadata['date'], DATE_FORMAT)

            except (KeyError, ValueError):
                metadata['ignore'] = True
                error('Could not convert date for {}; ignoring file.'.format(metadata['slug']))

        else:
            metadata['sort_date'] = dt.now()

    def __normalize_meta(self, metadata, file_slug):
        '''
        Adjusts or sets the values for each of the following dictionary keys in the
        Markdown metadata passed in:

        - date
        - sort_date
        - slug
        - type

        Returns the correct slug.
        '''
        metadata['ignore'] = False
        metadata['slug'] = metadata['slug'][0] if 'slug' in metadata.keys() else file_slug
        metadata['type'] = metadata['type'][0] if 'type' in metadata.keys() else 'post'
        self.__normalize_date(metadata)


