# -*- coding: utf-8 -*-
"""
btlxautoexpand.py
Bitelxux Oct-2016
"""

from genshi.builder import tag

from trac.core import *
from trac.wiki import IWikiSyntaxProvider


class BtlxAutoURL(Component):
    implements(IWikiSyntaxProvider)

    def __init__(self, *args, **kwargs):
        self.AutoExpandList = {}
        options = self.env.config.options('btlxautourl')
        for option in options:
            self.AutoExpandList[option[0]] = option[1]

        self.words = "|".join(r'\b[%s|%s]%s\b' % (k[0].lower(), k[0].upper(), k[1:]) \
                     for k in self.AutoExpandList.keys())

        super(BtlxAutoURL, self).__init__(*args, **kwargs)

    def get_link_resolvers(self):
        return []

    def get_wiki_syntax(self):
        if not self.words:
            return
        yield (r'(?P<keyword>(%s))' % self.words, 
               self._format_regex_link)

    def _format_regex_link(self, formatter, ns, match):
        self.env.log.debug('formatter: %s ns: %s' % (formatter, ns))
        keyword = match.group('keyword') or 'test'
        label= match.group(0)
        return tag.a(keyword, href=self.AutoExpandList[keyword.lower()])

