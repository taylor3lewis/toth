#!/usr/bin/python
# -*- coding: utf-8 -*-
from glob import glob
import regex
from generators.utils import defs as d
from generators.utils import filter_sentences as fs
from generators.utils import acutes_filter


def process_dict_files():
    buffer_entry = list()
    for file_ in glob('local_dicts/*.txt'):
        open('local_dicts/not_in_db/' + file_.split('/')[-1], 'w')
        dict_ = file(file_, 'r')
        for line in dict_.readlines():
            line = line.replace('\n', '')
            if line != '':
                buffer_entry.append(line.lower())
            else:
                term_def = clean_entry(buffer_entry)
                fs.get_syntactics_functions(term=term_def[0],
                                            text=term_def[1],
                                            filters=[d.VERBO])
                print '-' * 100
                buffer_entry = list()


def clean_entry(entry):
    term = None
    definition = ''
    for i, line in enumerate(entry):
        if i == 0:
            term = regex.sub(r'[\*,]', '', line)
            term = term.replace(' ', '')
            term = term.split('(')[0]
            term = term.split('^')[0]
        else:
            definition += ' ' + line
    return term, fs.get_syntactics_functions(definition,
                                             filters=[
                                                 d.SUBSTANTIVO
                                             ])


if __name__ == '__main__':
    process_dict_files()
