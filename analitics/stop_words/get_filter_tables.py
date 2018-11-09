# coding: utf-8
import re
import os
import sys
project_path = os.path.abspath(__file__).split('/')
del project_path[-1]
del project_path[-1]
del project_path[-1]
sys.path.append(os.path.join('/'.join(project_path), 'generators'))

from generators.utils.filter_tables import artigos
from generators.utils.filter_tables import adverbios
from generators.utils.filter_tables import preposicoes
from generators.utils.filter_tables import pronomes

from generators.utils.stop_words.adverbios import ADVERBIOS
from generators.utils.stop_words.preposicoes import PREPOSICOES
from generators.utils.stop_words.pronomes import PRONOMES

# from generators.utils.stop_words.adjetivos import ADJETIVOS
# from generators.utils.stop_words.numero import NUMERO

categories = {
    "artigos": {'list': artigos, 'exclusion': None},
    "adverbios": {'list': adverbios, 'exclusion': ADVERBIOS},
    "preposicoes": {'list': preposicoes, 'exclusion': PREPOSICOES},
    "pronomes": {'list': pronomes, 'exclusion': PRONOMES}
}

for category in categories.items():
    name = category[0]
    count = 0
    file_ = open('tb_all_' + name.lower() + '.txt', 'w')
    for it in category[1]['list']:
        if category[1]['exclusion'] is not None and (it in category[1]['list'] or '"' in it):
            continue
        el = '"' + it + '": None, '
        count += 1
        file_.write(el)
    file_.close()
    print count
