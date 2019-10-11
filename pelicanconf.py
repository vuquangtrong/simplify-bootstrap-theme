#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site info
AUTHOR = 'vuquangtrong'
ROBOTS = 'index, follow'

SITENAME = 'Simplify'
SITETITLE = 'Simplify'
SITESUBTITLE = 'A simple theme for blog, powered by Bootstrap and Pelican'
SITEDESCRIPTION = 'A simple theme for blog, powered by Bootstrap and Pelican'
SITELOGO = 'logo.png'

# when developing: don't specify URL, use document-relative URLs 
SITEURL = ''
RELATIVE_URLS = True

# Locale and Language
LOCALE = 'en_US'
DEFAULT_LANG = 'en'
TIMEZONE = 'Asia/Saigon'
DATE_FORMATS = {
    'en': '%b %d, %Y',
}

# Build settings
PATH = 'content'
THEME = './simplify-bootstrap-theme'

ARTICLE_PATHS = ['blog']
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_PRIMARY_PATH = 'blog'

PAGE_PATHS = [
    'pages'
]

DIRECT_TEMPLATES = [
    'index', 
    'authors', 
    'categories', 
    'tags', 
    'archives', 
    '404'
]

TEMPLATE_PAGES = {
    'pages/test.html': 'test.html'
}

DEFAULT_PAGINATION = 10
DEFAULT_DATE = (2010, 10, 10, 10, 10, 10)

OUTPUT_PATH = 'output/'
DELETE_OUTPUT_DIRECTORY = True

# Feed generation, usually not needed when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Advanced Settings
FORMATTED_FIELDS = [] # removed 'summary'
STATIC_PATHS = [
	'images',
	'favicon.ico',
    'logo.png',
	'.htaccess',
	'robots.txt'
]

# Plugins
PLUGIN_PATHS = [
    '../pelican-plugins'
]

PLUGINS = [
    'sitemap', # generate sitemap document, see <https://www.sitemaps.org>
    'post_stats', # generate post statistics
    'related_posts', # find articles those share common tags
    'neighbors' # find next, previous article 
]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

RELATED_POSTS_MAX = 5
RELATED_POSTS_SKIP_SAME_CATEGORY = False

# Markdown extensions
TYPOGRIFY = True
MARKDOWN = {
    'extensions': [
        # official extensions
        'markdown.extensions.extra', # include extensions: abbr, attr_list, def_list, fenced_code, footnotes, tables
        'markdown.extensions.codehilite', # to generate code color scheme using pygments
        'markdown.extensions.meta', # to parse key:value pairs at the begining of file
        'markdown.extensions.sane_lists',# for better list 
        'markdown.extensions.toc', # add Table of Content
        'markdown.extensions.nl2br', # easily to add new line, but make attr_list and legacy_attrs hard to control
        #'markdown.extensions.admonition', # to make  alert box
        #'markdown.extensions.legacy_attrs', # insert attribs into element, but markdown already has a built-in function that do the same thing
        #'markdown.extensions.legacy_em', # to use legacy emphasis
        #'markdown.extensions.smarty', # converts ASCII dashes, quotes and ellipses to their HTML entity equivalents
        #'markdown.extensions.wikilinks',

        # 3rd party extensions
        'markdown_checklist.extension', # show checkbox in list
        #'markdown_captions', # convert <img> to <figure> and <figcaption>
    ],
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
    },
    'output_format': 'html5',
}

# Social widget
SOCIAL = {
	'facebook': 'https://facebook.com/trongvq',
    'github': 'https://github.com/vuquangtrong',
    'twitter': '#',
}

# Site validation
# CLAIM_GOOGLE = ""
# CLAIM_BING = ""

# Comments
DISQUS_SITENAME = "vuquangtrong-github-io"

# Sharing
ADD_THIS_ID = "ra-5d9ffca0db80069e"

# Tracking and Ads
GOOGLE_ANALYTICS = "UA-42618265-2" # old method
# GOOGLE_SITE_TAG = "UA-42618265-2" # new method to use with Tag Manager
# GOOGLE_TAG_MANAGER = ""

GOOGLE_ADSENSE_ID = 'ca-pub-9105473411342324'

GOOGLE_ADSENSE_CONFIG = {
    'page_level_ads': False,
    'ads': {
        'aside': '',
        'main_menu': '',
        'index_top': '',
        'index_bottom': '',
        'article_top': '',
        'article_bottom': '',
    }
}

# HEAP_ANALYTICS = ""

MATOMO_SITENAME = 'vuquangtronggithubio' # new site of PIWIK

# PIWIK_SITE_ID = ""
# PIWIK_URL = ""
# PIWIK_SSL_URL = ""