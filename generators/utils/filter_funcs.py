#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import filter_tables


def filter_all(words, unique=True):
    if unique:
        temp_len = set()
        temp_words = set()
    else:
        temp_len = list()
        temp_words = list()

    # filter by length
    for word_len in words:
        if len(word_len) < 3:
            continue
        temp_len.add(word_len) if unique else temp_len.append(word_len)

    for w_ in temp_len:
        if (w_ in filter_tables.preposicoes or w_ in filter_tables.artigos
            or w_ in filter_tables.pronomes or w_ in filter_tables.adverbios):
            continue
        temp_words.add(w_) if unique else temp_words.append(w_)

    return temp_words


def filter_all_xxxx(words, unique=True):
    if unique:
        temp_len = set()
        temp_words_1 = set()
        temp_words_2 = set()
        temp_words_3 = set()
        temp_words_4 = set()
    else:
        temp_len = list()
        temp_words_1 = list()
        temp_words_2 = list()
        temp_words_3 = list()
        temp_words_4 = list()

    for word_len in words:
        if len(word_len) < 3:
            continue
        temp_len.add(word_len) if unique else temp_len.append(word_len)

    for word_1 in temp_len:
        if word_1 in filter_tables.preposicoes:
            continue
        temp_words_1.add(word_1) if unique else temp_words_1.append(word_1)

    for word_2 in temp_words_1:
        if word_2 in filter_tables.artigos:
            continue
        temp_words_2.add(word_2) if unique else temp_words_2.append(word_2)

    for word_3 in temp_words_2:
        if word_3 in filter_tables.pronomes:
            continue
        temp_words_3.add(word_3) if unique else temp_words_3.append(word_3)

    for word_4 in temp_words_3:
        if word_4 in filter_tables.adverbios:
            continue
        temp_words_4.add(word_4) if unique else temp_words_4.append(word_4)

    return temp_words_4


def remove_html_entities(text):
    temp_text = text
    for entity in filter_tables.entidades_html:
        temp_text = temp_text.replace(entity, "")
    temp_list_occurrences = re.findall(r"\&\#x.+?;", temp_text)
    for item in temp_list_occurrences:
        temp_text = temp_text.replace(item, "")
    return temp_text


def replace_html_entities(text):
    for html_entity in filter_tables.HTML_ENTITIES_TABLE_CODES:
        if html_entity[0] is not None and html_entity[0] in text:
            text = text.replace(html_entity[0], html_entity[2])
        if html_entity[1] is not None and html_entity[1] in text:
            text = text.replace(html_entity[1], html_entity[2])
    return text


if __name__ == '__main__':
    print re.match(r"[^ab]", "chico")
    print re.match(r"[^ab]", "batata")
