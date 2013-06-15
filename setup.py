from setuptools import setup

requires = ['Markdown', 'PyRSS2Gen', 'Pygments', 'PyYAML >= 3.10', 'typogrify']
packages = ['step_stool']
entry_points = {
    'console_scripts': [
        'step-stool = step_stool:main'
    ]
}

classifiers = [
    'Environment :: Console',
    'Development Status :: 1 - Planning',
    'Intended Audience :: End Users/Desktop'
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English'
    'Operating System :: OS Independent'
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.3',
    'Topic :: Communications'
]

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
    classifiers=classifiers
)

