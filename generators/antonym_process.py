#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from utils import db_utils
from utils import defs as d
from unidecode import unidecode
from bs4 import BeautifulSoup

target_page = r"https://www.antonimos.com.br/"

frag = u"ua"
word_stop = "xxxxx"

breakpoint = "breakpoint_" + frag


def process_all_words():
    lock = True
    lock_inner = False
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
                    if lock_inner:
                        if term['nid'] == word_stop:
                            lock_inner = False
                        else:
                            continue
                    # --------------------------------------------
                    print len(result), term["nid"], "-" * 50
                    try:
                        if reverse_alphabet:
                            open(breakpoint + '_r.txt', 'w').write(str(combination + ":" + term['nid']))
                        else:
                            open(breakpoint + '.txt', 'w').write(str(combination + ":" + term['nid']))
                    except:
                        pass
                    # ------------- #
                    # process lemma #
                    if process_antonym(term['nid']) is None:
                        print 'unable to get page:', target_page + unidecode(unicode(term['nid']))
                        pass
                    else:
                        print term['nid'], 'already done'
                    continue


def process_antonym(word):
    try:
        content = requests.get(target_page + unidecode(unicode(word))).content
        soup = BeautifulSoup(content, 'lxml')
        for i, meaning in enumerate(soup.findAll('div', {'class': 's-wrapper'})):
            if i == 0:
                print "Antônimos"
                for rel_word in meaning.findAll('a'):
                    db_utils.create_relationship(rel_word.text.lower(), word.lower(), d.R_ANTONYM)
            else:
                print "Campo Antonômicos", i
                for rel_word in meaning.findAll('a'):
                    if db_utils.check_rel_between_nodes(rel_word.text.lower(), word.lower(), d.R_ANTONYM) == 0:
                        db_utils.create_relationship(rel_word.text.lower(), word.lower(), d.R_ANTONYM_FIELD)
        return True
    except Exception as error:
        print error, target_page + unidecode(unicode(word))


if __name__ == '__main__':
    process_all_words()
    # process_antonym('morte')