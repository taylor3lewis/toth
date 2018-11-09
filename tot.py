#!/usr/bin/python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    letters = "abcdefghijklmnopqrstuvwxyzáàãâäéèêëíìîïóòõôöúùûüçñ".decode(encoding='utf-8')
    alphabet = [[l2 + l1 for l1 in letters] for l2 in letters]
    for ll in alphabet:
        for pair in ll:
            print pair
