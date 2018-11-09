#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from generators.utils import acutes_filter
from generators.utils import scrapper
from generators.utils import db_utils
from generators.utils import defs as d
from unidecode import unidecode
from bs4 import BeautifulSoup

target_page = r"http://www.sinonimos.com.br/"
divisor_begin = '<div class="s-wrapper">'  # <div class="s-wrapper">
breakpoint = "breakpoint"
frag = u"qu"
word_stop = "quimerizaríamos"


def process_all_words():
    lock = False
    reverse_alphabet = True
    letters = "abcdefghijklmnopqrstuvwxyzáàãâäéèêëíìîïóòõôöúùûüçñ".decode(encoding='utf-8')
    alphabet = [[l2 + l1 for l1 in letters] for l2 in letters]
    for letter_combination in sorted(alphabet, reverse=reverse_alphabet):
        for combination in letter_combination:
            print "+" * 50
            print combination
            if lock:
                if frag == combination:
                    lock = False
                else:
                    continue
            open(breakpoint + '_r.txt', 'w').write(str(combination))
            db_utils.remove_relationship_overly_semantics(combination)


def process_semantic_relationships(word):
    try:
        page = scrapper.get_html(target_page + unidecode(unicode(word)), print_erros=False)
        if page is None:
            return None

        soup = BeautifulSoup(page, 'html.parser')
        for i, meaning in enumerate(soup.findAll('div', {'class': 's-wrapper'})):
            if i == 0:
                print "sinonimos"
                for rel_word in meaning.findAll('a', {'class': 'sinonimo'}):
                    db_utils.create_relationship(rel_word.text.lower(), word.lower(), d.R_SYNONYMOUS)
            else:
                print "campos"
                for rel_word in meaning.findAll('a', {'class': 'sinonimo'}):
                    db_utils.create_relationship(rel_word.text.lower(), word.lower(), d.R_SEMANTICS)
        return True
    except Exception as error:
        print error, target_page + unidecode(unicode(word))


if __name__ == '__main__':
    process_all_words()
    # process_semantic_relationships('morte')
