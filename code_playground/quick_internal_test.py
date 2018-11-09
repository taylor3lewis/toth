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
        print "node not found", word_to_check
        return True
    elif BINARY_SENTIMENT in node.properties:
        try:
            current_polarity = node.properties[BINARY_SENTIMENT]
            if polarity == current_polarity:
                print "Already setted:", word_to_check, '=>',
                return True
            else:
                print "NEUTRALIZING ambiguous lemma", word_to_check, '=>',
                db_utils.add_property(word_to_check, BINARY_SENTIMENT, 0)
                return False
        except Exception as err:
            print str(err), word_to_check
            return True
    else:
        return False


if __name__ == '__main__':
    word = "luxúria"
    bs = -1
    polarity = GOOD if bs > 0 else BAD
    check_sentiment_status_error(word, polarity)

