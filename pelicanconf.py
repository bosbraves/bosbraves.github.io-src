#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

LOAD_CONTENT_CACHE = False

AUTHOR = 'Ryan Mills'
SITENAME = "Ryan's Blog"
SITEURL = ''

PATH = 'content'
THEME = 'themes/minimalX'

TIMEZONE = 'America/New_York'
LOCALE = 'usa'
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%B %d, %Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Other options
STATIC_PATHS = ['images', 'authors']

IGNORE_FILES = ['.ipynb_checkpoints']

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/bosbraves'),
          ('linkedin', 'https://www.linkedin.com/in/ryancmills'),)

SHARE_BUTTONS = ('github', 'linkedin', 'twitter', 'mail')

# Pagination after more than 4 articles
DEFAULT_PAGINATION = 4

SUMMARY_MAX_LENGTH = 70

USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'General'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True

# Plugins
TAG_CLOUD = True
# Tagcloud Settings
TAG_CLOUD_STEPS = 5
TAG_CLOUD_MAX_ITEMS = 50
TAG_CLOUD_BADGE = True
TAG_CLOUD_SORTING = 'size'

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud"]

# Author Pages
AUTHOR_PAGE_PATH = 'authors'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

