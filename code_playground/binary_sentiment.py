# coding: utf-8
import os
import sys
project_path = os.path.abspath(__file__).split('/')
del project_path[-1]
del project_path[-1]
sys.path.append(os.path.join('/'.join(project_path), 'generators'))
from generators.utils import db_utils
from generators.utils import defs as d
# import re
# from generators.utils.filter_tables import breakable_sentence_chars
# from generators.utils import filter_tables as ft


BINARY_SENTIMENT = d.BINARY_SENTIMENT
BAD = -1
GOOD = 1


def save_not_found(word_not_found):
    file_ = open('not_found.txt', 'a')
    file_.write(word_not_found + '\n')
    file_.close()


def check_sentiment_status_error(word_to_check, polarity):
    node = db_utils.get_node(word_to_check)
    if node is None:
        save_not_found(word_to_check)
        return True
    elif BINARY_SENTIMENT in node.properties:
        try:
            current_polarity = node.properties[BINARY_SENTIMENT]
            if polarity == current_polarity:
                print "Already setted".ljust(30), word_to_check
                return True
            else:
                print "NEUTRALIZING ambiguous lemma".ljust(30), word_to_check, '=>',
                db_utils.add_property(word_to_check, BINARY_SENTIMENT, 0)
                return False
        except Exception as err:
            print str(err), word_to_check
            return True
    else:
        return False


def deep_semantic_digg(word_ds, break_point=True):
    db_utils.add_property(word_ds, BINARY_SENTIMENT, polarity)
    sf_type = db_utils.get_semantic_fields_to_word_without_proper(word_ds, BINARY_SENTIMENT)
    if not sf_type:
        print "No avaliable semantic field to %s!!!" % word_ds
    else:
        if not break_point:
            print sf_type
        for w in sf_type:
            # if False: # FORCE FIX
            #     db_utils.add_property(w, BINARY_SENTIMENT, polarity)
            #     print "Setted    ", w, polarity
            #     continue
            if not check_sentiment_status_error(w, polarity):
                db_utils.add_property(w, BINARY_SENTIMENT, polarity)
                print "Setted".ljust(30), w, polarity


bs = -1
polarity = GOOD if bs > 0 else BAD

if __name__ == '__main__':
    word = "covarde"
    deep_semantic_digg(word, False)




















