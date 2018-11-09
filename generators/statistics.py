#!/usr/bin/python
# -*- coding: utf-8 -*-

from utils import db_utils
letters = "abcdefghijklmnopqrstuvwxyzáàãâäéèêëíìîïóòõôöúùûüçñ".decode(encoding='utf-8')

total_sylabus = {}
for letter in letters:
    count = db_utils.count_pattern(letter+".+?")
    total_sylabus[letter] = count
    print letter, count


alphabet = [[l2 + l1 for l1 in letters] for l2 in letters]
for letter_combination in alphabet:
    for combination in letter_combination:
        count = db_utils.count_pattern(combination + ".+?")
        if count > 9999:
            print combination[0], total_sylabus[combination[0]], '|', combination, count
