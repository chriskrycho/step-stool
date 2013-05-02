{this project}
==============

A static website generator (in Python).

Introduction
------------

{this project} is a simple static site generator. You write your content in
[Markdown][md], run a quick command line script, and it gets published to the
web. No content management system, no database, just simple HTML files.

{this project} supports custom templates (via [Jinja2][jinja]), so you can make
your site look pretty much however you want. You can apply different templates
to different sections of your site, using a single line in a configuration file.

{this project} also allows you to structure your site pretty much however you
choose. If you want to have nested categories, go for it. If you want an
entirely flat structure with an ever-growing list of tags, you can do that, too.

Setup
-----
### Installation
#### Dependencies

To install {this project}, you'll need at least [Python 3.0][python]. If you
don't have it, you'll need to get it:

- [Download it][python] and install it manually.
- Use a package manager to install it (e.g. `brew install python`, ``, etc.).

That's it. (All the Python package dependencies will take care of themselves
when you install the package.)

#### Walkthrough

The easiest way to install {this project} is using `pip`, which also installs
all dependencies for using {this project}:

    :::bash
    $ pip install {this project}

I recommend using a virtual environment for this install, to keep it separate
from your other (system or project) Python setups. If you have
[virtualenvwrapper][vw] installed:

    :::bash
    $ mkvirtualenv {this project}
    $ setvirtualenvproject /path/where/you/want/to/build/your/site
    $ pip install {this project}

Otherwise, since we're running Python 3, you can just do (preferably in a
virtual environments directory somewhere in your home folder or some such):

    :::bash
    $ pyvenv {this project} $ pip install {this project}

Alternatively, you can download the package manually from the [downloads
page][download] and run `python setup.py`.

### Configuration


[download]: /

[jinja]: http://jinja.pocoo.org/ "Jinja 2 Python Templating Language"

[md]: http://daringfireball.net/projects/markdown/

[python]: http://www.python.org/download/ "Download Python 3 for your platform"

[vw]: https://bitbucket.org/dhellmann/virtualenvwrapper "Extensions to Ian Bickings virtualenv tool"