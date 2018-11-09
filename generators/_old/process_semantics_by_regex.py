#!/usr/bin/python
# -*- coding: utf-8 -*-
from generators.utils import scrapper
from generators.utils import db_utils
from generators.utils import defs as d
from unidecode import unidecode
from bs4 import BeautifulSoup
import urllib
import requests


target_page = r"http://www.sinonimos.com.br/"
divisor_begin = '<div class="s-wrapper">'  # <div class="s-wrapper">
breakpoint = "process_by_regex"
word_stop = "cadela"
criteria = ".+?['].+?"


def process_all_words():
    lock_inner = False
    # -----------------------------------------------------------------------------
    result = db_utils.get_nodes_nids_by_regex(criteria)
    # -----------------------------------------------------------------------------
    if result:
        # Sort Result Alphabetically ----------------------
        for term in sorted(result, key=lambda k: k['nid']):
            if lock_inner:
                if term['nid'] == word_stop:
                    lock_inner = False
                else:
                    continue
            # --------------------------------------------
            try:
                open(breakpoint + '.txt', 'w').write(str(term['nid']))
            except:
                pass
            # --------------------------------------------
            # process lemma
            single_term = urllib.quote(str(term["nid"]))

            if process_semantic_relationships(single_term) is None:
                print 'unable to get page:', target_page + unidecode(unicode(term['nid']))
                # db_utils.add_label_to_node(term['nid'], d.R_NOT_IN_WEB)
                pass
            else:
                print term['nid'], 'already done'
            continue
    else:
        print "No nodes match the criteria", criteria


def process_semantic_relationships(word):
    try:
        page = requests.get(target_page + word).content
        soup = BeautifulSoup(page, 'html.parser')
        result = soup.findAll('div', {'class': 's-wrapper'})
        for i, meaning in enumerate(result):
            if i == 0:
                print "sinonimos"
                for rel_word in meaning.findAll('a', {'class': 'sinonimo'}):
                    print rel_word
                    db_utils.create_relationship(rel_word.text.lower(), word.lower(), d.R_SYNONYMOUS)
            else:
                print "campos"
                for rel_word in meaning.findAll('a', {'class': 'sinonimo'}):
                    print rel_word
                    db_utils.create_relationship(rel_word.text.lower(), word.lower(), d.R_SEMANTICS)
        return True
    except Exception as error:
        print error, target_page + unidecode(unicode(word))


if __name__ == '__main__':
    process_all_words()
