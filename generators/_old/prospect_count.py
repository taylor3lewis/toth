#!/usr/bin/python
# -*- coding: utf-8 -*-
from generators.utils import db_utils


letters = "abcdefghijklmnopqrstuvwxyzáàãâäéèêëíìîïóòõôöúùûüçñ".decode(encoding='utf-8')
alphabet = [[l2 + l1 for l1 in letters] for l2 in letters]
for letter_combination in alphabet:
    for combination in letter_combination:
        count = db_utils.count_pattern(combination + ".+")
        if count > 9999:
            print combination, count

# ab 13735
# ac 15982
# al 14469
# am 11119
# ap 13877
# ar 12710
# ca 21710
# co 32696
# de 105240
# em 17289
# en 49875
# es 44459
# in 17911
# ma 15445
# pa 12771
# pe 10760
# pr 15121
# re 48089
# so 10549
# su 10613
# tr 16032
