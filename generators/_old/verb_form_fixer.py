#!/usr/bin/python
# -*- coding: utf-8 -*-
from generators.utils import db_utils
from generators.utils import defs as d


if __name__ == '__main__':
    result = db_utils.get_nodes_nids_by_regex(".+?/.+?", label=d.CONJUGACAO)
    if result:
        for term in result:
            rel_data = db_utils.get_conjugation_root(term['nid']).data()
            for data in rel_data:
                c = data['c']
                r = data['r']
                v = data['v']

                print c['nid']
                if v is None:
                    print "WTF!?", c
                    continue

                tense_unique = term['nid'].split('/')
                for tense in tense_unique:
                    print '\t', tense
                    verb_n = db_utils.get_node(v['nid'], label=d.VERBO)
                    if db_utils.get_node(tense, label=d.CONJUGACAO) is None:
                        tense_n = db_utils.create_tense(tense)
                        if tense_n is not None and verb_n is not None:
                            print '\t\tInserido:', tense
                            db_utils.create_tense_relationship(tense_n['nid'], verb_n['nid'], d.R_VERB_TENSE)
                        else:
                            print '\t\tJá tem:', tense
                    else:
                        print '\t\tJá tem:', tense

                db_utils.delete_conjugation_wrong(term['nid'])
                print '-' * 100
