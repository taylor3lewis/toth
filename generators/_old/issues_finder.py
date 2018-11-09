#!/usr/bin/python
# -*- coding: utf-8 -*-
from glob import glob
from unidecode import unidecode
from generators.utils import scrapper
import re
import regex
from generators.utils import db_utils

target_page = r"http://www.sinonimos.com.br/"
divisor_begin = '<div class="s-wrapper">'  # <div class="s-wrapper">


def find_fails():
    # file_ = 'simple_dict_outputs/word_queries/file_query1.txt'
    fails = open('fails2B.txt', 'w')
    for file_ in glob('simple_dict_outputs/word_queries/*'):
        open('file_prog2B.txt', 'a').write(file_ + "\n")
        queries = open(file_, 'r')
        for query in queries.readlines():
            word = query.replace('\n', '').split('"')[1]
            test = regex.match(r"[áàãâäéèêëíìîïóòõôöúùûüçñÁÀÃÂÄÉÈÊËÍÌÎÏÓÒÕÖÔÚÙÛÜÇ]",
                               word,
                               re.UNICODE)
            if test:
                fails.write(query)
    fails.close()


def find_duplicates_nodes():
    for file_ in glob('simple_dict_outputs/word_queries/*'):
        queries = open(file_, 'r')
        for query in queries.readlines():
            word = query.replace('\n', '').split('"')[1]
            data = db_utils.get_node(nid=word)
            # break
        break


if __name__ == '__main__':
    find_duplicates_nodes()
