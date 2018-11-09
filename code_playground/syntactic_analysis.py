# coding: utf-8
import os, sys
project_path = os.path.abspath(__file__).split('/')
del project_path[-1]
del project_path[-1]
sys.path.append(os.path.join('/'.join(project_path), 'generators'))
import re
from generators.utils.filter_tables import breakable_sentence_chars
from generators.utils import db_utils
from generators.utils import defs as d
from generators.utils import filter_tables as ft


if __name__ == '__main__':
    text = "A paixão dos suicidas que se matam sem explicação"
    text = text.lower()
    for word in text.split(' '):
        w_type = db_utils.get_word_type(word)
        if not w_type:
            print word
        else:
            print word, w_type
