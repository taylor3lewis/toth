#!/usr/bin/python
# -*- coding: utf-8 -*-
import regex
import acutes_filter
import db_utils


def get_syntactics_functions(term, text, filters):
    # verify if term exists
    # first, clean sentence...
    text = acutes_filter.strip_non_text(text)
    text = text.split(' ')
    buffer_text = [frag for frag in text if len(frag) > 1]

    semantic_field = list()

    for word in buffer_text:
        # noinspection PyBroadException
        try:
            search_result = db_utils.get_node(word)
            if search_result:
                labels = search_result.labels()
                if labels:
                    for label in labels:
                        if label in filters:
                            semantic_field.append(search_result)
        except Exception as error:
            print "Something goes wrong to word: %s" % word, str(error)

    if semantic_field:
        return semantic_field
