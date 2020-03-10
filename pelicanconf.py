#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Devin'
SITENAME = u'Devin Brady Consulting'
SITEURL = 'https://devinbrady.com'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Medium', 'https://medium.com/@devinbrady'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/devinbrady'),
          ('Twitter', 'https://twitter.com/bradyhunch'),
          ('LinkedIn', 'https://www.linkedin.com/in/devin-brady/'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images']

THEME = "./theme/pelican-bootstrap3/"

PLUGIN_PATHS = ['/Users/devin/Projects/pelican-plugins', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}