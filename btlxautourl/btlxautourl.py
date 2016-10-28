# -*- coding: utf-8 -*-
"""
btlxautourl.py
Bitelxux Oct-2016


This is a plugin for trac that automatically expands
words defined in section [btlxautourl] from trac.ini
to the URLs defined.

e.g.

[btlxautourl]
google = http://www.google.com
starwars = http://www.starwars.com

Then, all the words "google" and "starwars" will be
rendered automatically as links to their URLs. Not need any
more of typing [[http://bla.ble.blu|text]]

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
            self.AutoExpandList[option[0].lower()] = option[1]

        # Too complex regular until I either found out how to use compiled
        # regulars with re.IGNORECASE or how to ignore case without compile
        # ( at this moment, (?i) does not work )
        self.words = "|".join("".join( r'[%s|%s]' %(word[i].lower(),
                                                    word[i].upper()) for i in
                                                    range(len(word)))
                         for word in self.AutoExpandList.keys())

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
