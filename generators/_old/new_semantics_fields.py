#!/usr/bin/python
# -*- coding: utf-8 -*-
from generators.utils import scrapper
from generators.utils import db_utils
from generators.utils import defs as d
from unidecode import unidecode
from bs4 import BeautifulSoup

target_page = r"http://www.sinonimos.com.br/"
divisor_begin = '<div class="s-wrapper">'  # <div class="s-wrapper">
breakpoint = "breakpoint"
frag = u"de"
word_stop = "desesperado"


def process_all_words():
    lock = True
    lock_inner = True
    reverse_alphabet = False
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
            # -----------------------------------------------------------------------------
            result = db_utils.get_nodes_nids_by_regex("%s.+?" % combination)
            # -----------------------------------------------------------------------------
            if result:
                # Sort Result Alphabetically ----------------------
                for term in sorted(result, key=lambda k: k['nid']):
                    # if word_stop == term["nid"]:
                    #     lock_inner = False
                    #     continue
                    if "'" in term["nid"]:
                        continue
                    if lock_inner:
                        if term['nid'] == word_stop:
                            lock_inner = False
                        else:
                            continue
                    # --------------------------------------------
                    print len(result), term["nid"], "-" * 50
                    try:
                        if reverse_alphabet:
                            open(breakpoint + '_' + frag + '_r.txt', 'w').write(str(combination + ":" + term['nid']))
                        else:
                            open(breakpoint + '_' + frag + '.txt', 'w').write(str(combination + ":" + term['nid']))
                    except:
                        pass
                    # --------------------------------------------
                    # process lemma
                    if process_semantic_relationships(term['nid']) is None:
                        print 'unable to get page:', target_page + unidecode(unicode(term['nid']))
                        db_utils.add_label_to_node(term['nid'], d.R_NOT_IN_WEB)
                        pass
                    else:
                        print term['nid'], 'already done'
                    continue


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
