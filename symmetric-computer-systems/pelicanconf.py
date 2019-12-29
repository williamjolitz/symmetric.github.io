#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'William Jolitz'
SITENAME = 'Paleocomputing: restoring the artefacts of Silicon Valley, a tale'
SITEURL = 'https://williamjolitz.github.io/symmetric-computer-systems/'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_RSS = 'feeds/{slug}.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

# Blogroll
LINKS = (('386bsd', 'https://386bsd.org'),
         ('386bsd repository', 'https://github.com/386bsd/386bsd'),
        )

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/williamjolitz/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True