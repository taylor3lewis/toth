# coding: utf-8
import os
import sys
project_path = os.path.abspath(__file__).split('/')
del project_path[-1]
del project_path[-1]
sys.path.append(os.path.join('/'.join(project_path), 'generators'))
import re
from generators.utils.filter_tables import breakable_sentence_chars
from generators.utils import db_utils
from generators.utils import defs as d
from generators.utils import filter_tables as ft


def parse_sentence(sentence):
    sentence = re.split(breakable_sentence_chars, sentence)
    sentence = [w.lower() for w in sentence if w]
    return sentence


def get_sentence_analisys(sentence):
    sentence = parse_sentence(sentence)
    for w in sentence:
        result = db_utils.get_nodes(w)
        print w, [list(n['n'].labels())[0] for n in result.data()]


def get_semantic_sents(sentence):
    sentence = parse_sentence(sentence)
    for w in sentence:
        print w


def get_semantic_fields(word):
    if db_utils.check_word_type(word, d.SUBSTANTIVO):
        return db_utils.get_semantic_fields_to_word(word)


def get_semantic_structure(sentence):
    analisys = list()
    sentence = sentence.lower()
    parse_sentences = sentence.split(',')
    for frag in parse_sentences:
        frag_analisys = list()
        sentence = re.sub(ft.parse_chars, '', frag)
        for word in [w for w in sentence.split(' ') if w]:
            words = db_utils.get_word_type(word)
            frag_analisys.append({'word': word, 'types': words})
        analisys.append(frag_analisys)
    return analisys


def walk_through_semantic_structure(sentence):
    structure = get_semantic_structure(sentence)
    for frag in structure:
        for w in range(0, len(frag) - 1):
            if w == 0 or w == len(frag):
                continue
            else:
                process_word_types_by_siblings(frag[w - 1], frag[w], frag[w + 1])


def process_word_types_by_siblings(w1, w2, w3):
    if len(w1['types']) > 1 or len(w1['types']) > 1 or len(w1['types']) > 1:
        print w1, w2, w3
    else:
        print 'nothing to process'


if __name__ == "__main__":
    for id, i in enumerate(get_semantic_fields('chuva')):
        print id
        print ",".join(i)
        print '-'*100
    walk_through_semantic_structure("A demência nasce em flor")
    # walk_through_semantic_structure("A demência nasce em flor, não em pétala")
