#!/usr/bin/python
# -*- coding: utf-8 -*-
from generators.utils import db_utils
from generators.utils import defs as d

breakpoint = False
breakpoint_lemma = 'sacar'


def process_all_words():
    letters = "abcdefghijklmnopqrstuvwxyzáàãâäéèêëíìîïóòõôöúùûüçñ".decode(encoding='utf-8')
    alphabet = [[l2 + l1 for l1 in letters] for l2 in letters]
    for letter_combination in alphabet:
        for combination in letter_combination:
            # -----------------------------------------------------------------------------------
            result = db_utils.get_nodes_nids_by_regex("%s.+?" % combination, label=d.SUBSTANTIVO)
            # -----------------------------------------------------------------------------------
            if result:
                for term in result:
                    try:
                        open('breakpoint.txt', 'w').write(str(combination))
                    except:
                        pass
                    # if term['nid'] == breakpoint_lemma:
                    #     breakpoint = True
                    #     continue
                    if db_utils.verify_node_oneness(term['nid'], label=d.SUBSTANTIVO):
                        continue
                    else:
                        print "DUPLICADO:", term['nid']
        break


if __name__ == '__main__':
    process_all_words()
