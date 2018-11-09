#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import urllib2
import re

reload(sys)
sys.setdefaultencoding('utf8')

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'

MOCK_HEADERS = {
    'User-Agent': user_agent,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

REMOVE = [" &ndash;", "para", "eu", "tu", "não", "ele/ela", "eles/elas", "nós", "vós"]


def get_html(page=None):
    """
    page: string with all HTML
    """
    if page is not None:
        request = urllib2.Request(page, headers=MOCK_HEADERS)
        response = urllib2.urlopen(request).read()
        return response


def html_to_word_mutations(verb_search):
    url_formed = "http://www.conjuga-me.net/verbo-" + verb_search.lower()
    html = get_html(page=url_formed)
    if 'encontrado</p>' in html:
        return None
    words = re.findall(r"class=\"output\".*?>.+?</td>", html)
    verb_mutations_inside = set()
    for it in words:
        it = re.sub(r"class=\"output\".*?>", "", it)
        it = re.sub(r"<.+?>", "", it)
        it = re.sub(r"</.*?>", "", it)
        it = unicode(it, encoding='ISO-8859-1')
        it = it.decode('utf-8')
        it = it.replace("  ", " ")
        for remove_this in REMOVE:
            it = it.replace(remove_this, "")
        it = it.replace(' ', '')
        if it == '' or it == ' ' or it == '\n':
            continue
        verb_mutations_inside.add(it)
    return verb_mutations_inside


def create_string_verb(main_verb, verb_forms):
    line_inside = main_verb.upper() + ":"
    if len(verb_forms) != 0:
        line_inside += ",".join(verb_forms)
        line_inside = line_inside.replace('/', ',').replace('is&asymp;', ',').replace('&asymp;', ',')
        return line_inside
    else:
        return None


def append_line(verb_line):
    file_result = open("verbs_list.TXT", "a")
    file_result.write(verb_line + '\n')
    file_result.close()
