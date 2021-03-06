#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITETITLE = 'Bruin Racing'
SITENAME = u"Bruin Racing"
SITEURL = ''
# SITEURL = 'http://www.bruinracing.com'
# SITEURL = 'http://staging.bruinracing.com'

AUTHOR = u'Lisa Morrison'

# GITHUB_URL = 'https://github.com/ejmorrison16'

TWITTER_NAME = 'bruinracing'
FACEBOOK_NAME = 'bruinracing'
INSTAGRAM_NAME = 'bruinracing'
# FACEBOOK_APPID = '169571003071390'
GOOGLE_ANALYTICS = 'UA-7881029-17'

SITESUBTITLE = 'Bruin Racing'
SITEDESCRIPTION = 'Student motor racing teams at UCLA'

SITELOGO = SITEURL + '/images/logo.png'
FAVICON = SITEURL + '/images/logo/racing_tab_logo.png'

BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

# COPYRIGHT_YEAR = 2019

MAIN_MENU = True

PATH = 'content'
PLUGIN_PATHS = ['plugins']
PLUGINS = ["pelican_alias", 'sitemap']
STATIC_PATHS = ['images', 'extra', 'files', 'share']
ARTICLE_EXCLUDES = ['extra']

THEME = 'theme'

TIMEZONE = 'US/Pacific'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
# FEED_DOMAIN = SITEURL
# FEED_ATOM = 'feeds/atom.xml'
FEED_ATOM = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly',
    },
    'exclude': ['tag/', 'category/']
}

# global metadata to all the contents
# DEFAULT_METADATA = {'yeah': 'it is'}

EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'},
    'extra/robots.txt': {'path': 'robots.txt'},
    # This is how you put a file in the root directory to validate control of
    # the domain for google
    # 'extra/google700c1f01b6b0e74c.html': {'path': 'google700c1f01b6b0e74c.html'},
    'extra/custom.css': {'path': 'static/custom.css'},
}
CUSTOM_CSS = 'static/custom.css'

# TEMPLATE_PAGES = {'content/pages/books.html': 'dest/books.html',
#                   'src/resume.html': 'dest/resume.html',
#                   'src/contact.html': 'dest/contact.html'}

INDEX_SAVE_AS = 'blog/index.html'
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
