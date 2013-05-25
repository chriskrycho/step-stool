from setuptools import setup

requires = ['Markdown', 'PyRSS2Gen', 'Pygments', 'PyYAML >= 3.10']
extras_require = ['mdx-smartypants']
packages = ['step-stool']
entry_points = {}

try:
    import argparse
except ImportError:
    requires.append('argparse')

README = open('README.md').read()

setup(
    name='step-stool',
    version='0.1',
    url='http://step-stool.io',
    description='A(nother) static site generator in Python',
    author='Chris Krycho',
    author_email='chris@step-stool.com',

    packages=packages,
    install_requires=requires,
    entry_points=entry_points,

    extras_require=extras_require
)

