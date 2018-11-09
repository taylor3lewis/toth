#!/usr/bin/python
# -*- coding: utf-8 -*-
from generators.utils import db_utils
from generators.utils import defs as d
import regex
breakpoint = False
breakpoint_lemma = 'sacar'


def process_tenses_for_single_verb(verb):
    result = db_utils.get_nodes_nids_by_regex(verb, label=d.VERBO)
    if result:
        for term in result:
            if db_utils.verify_node_oneness(term['nid'], label=d.VERBO):
                for term_property in term.properties.iteritems():
                    if term_property[0] in d.VERB_TENSES:
                        for tense in term_property[1]:
                            tenses_collection = regex.split(r"[,\/]", tense)
                            tenses_unique = set()
                            for tense_ in tenses_collection:
                                if '-' == tense_:
                                    continue
                                for tense_parentheses in tense_.split('('):
                                    tenses_unique.add(tense_parentheses.replace(')', ''))
                                for tense_unique in tenses_unique:
                                    if db_utils.get_node(tense_unique, label=d.CONJUGACAO) is not None:
                                        continue
                                    # Create relationship
                                    verb_n = db_utils.get_node(term['nid'], label=d.VERBO)
                                    tense_n = db_utils.create_tense(tense_unique)
                                    if tense_n is not None and verb_n is not None:
                                        db_utils.create_tense_relationship(term['nid'], tense_unique, d.R_VERB_TENSE)
                                        print '\r', tense_unique,
                                    else:
                                        print "Fodeu, %s ou %s não existem" % (term['nid'], tense_unique)
            else:
                from unidecode import unidecode
                print "Fodeu, " + unidecode(term['nid']) + " tá duplicado"
            print '\r', term['nid'], "completed!"
            print '-' * 100


def process_tenses():
    letters = "abcdefghijklmnopqrstuvwxyzáàãâäéèêëíìîïóòõôöúùûüçñ".decode(encoding='utf-8')
    alphabet = [[l2 + l1 for l1 in letters] for l2 in letters]
    for letter_combination in alphabet:
        for combination in letter_combination:
            result = db_utils.get_nodes_nids_by_regex("%s.+?" % combination, label=d.VERBO)
            if result:
                for term in result:
                    try:
                        open('breakpoint.txt', 'w').write(term['nid'])
                    except:
                        pass
                    if term['nid'] == breakpoint_lemma:
                        breakpoint = True
                        continue

                    if not breakpoint:
                        print term['nid'], 'already done'
                        continue

                    if db_utils.verify_node_oneness(term['nid'], label=d.VERBO):
                        for term_property in term.properties.iteritems():
                            if term_property[0] in d.VERB_TENSES:
                                for tense in term_property[1]:
                                    tenses_collection = regex.split(r"[,\/]", tense)
                                    tenses_unique = set()
                                    for tense_ in tenses_collection:
                                        if '-' == tense_:
                                            continue
                                        for tense_parentheses in tense_.split('('):
                                            tenses_unique.add(tense_parentheses.replace(')', ''))
                                        for tense_unique in tenses_unique:
                                            if db_utils.get_node(tense_unique, label=d.CONJUGACAO) is not None:
                                                continue
                                            # Create relationship
                                            verb_n = db_utils.get_node(term['nid'], label=d.VERBO)
                                            tense_n = db_utils.create_tense(tense_unique)
                                            if tense_n is not None and verb_n is not None:
                                                db_utils.create_tense_relationship(term['nid'], tense_unique, d.R_VERB_TENSE)
                                                print '\r', tense_unique,
                                            else:
                                                print "Fodeu, %s ou %s não existem" % (term['nid'], tense_unique)
                    else:
                        from unidecode import unidecode
                        print "Fodeu, " + unidecode(term['nid']) + " tá duplicado"
                    print '\r', term['nid'], "completed!"
                    print '-' * 100


if __name__ == '__main__':
    process_tenses_for_single_verb('saber')
