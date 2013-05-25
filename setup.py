from distutils.core import setup

requires = ['Markdown', 'mdx-smartypants', 'Pygments', 'PyYAML >= 3.10']
packages = ['step-stool']

try:
    import argparse
except ImportError:
    requires.append('argparse')

README = open('README.md').read()

setup(
    name='step-stool',
    version='0.1',
    url='http://step-stool.io',
    py_modules='step-stool.py',
    packages=packages
)

