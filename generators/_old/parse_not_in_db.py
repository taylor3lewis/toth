#!/usr/bin/python
# -*- coding: utf-8 -*-
from generators.utils import db_utils

expressions = set()
verb_tense = set()
words_plurals = set()
words = set()

total_counter = 0

file_ = open("not_in_db.txt", "r")
for line in file_.read().split('\n'):
    if line:
        total_counter += 1
        if " " in line:
            expressions.add(line)
        elif line.endswith("-se"):
            verb_tense.add(line)
        elif line.endswith("s"):
            words_plurals.add(line)
        else:
            words.add(line)
file_.close()

print "expressions", len(expressions)
print "verbos", len(verb_tense)
print "plurais", len(words_plurals)
print "palavras", len(words)

counter = 0
for token in words_plurals:
    counter += 1
    if db_utils.find_by_plural(token) is None:
        print counter, token
        f = open('even_not_in_db_plurals.txt', 'a')
        f.write(token+"\n")
        f.close()
