# coding: utf-8
import re
import os
import sys
import datetime
project_path = os.path.abspath(__file__).split('/')
del project_path[-1]
del project_path[-1]
del project_path[-1]
sys.path.append(os.path.join('/'.join(project_path), 'generators'))

begin = datetime.datetime.now()
count = 0

from generators.utils.stop_words.artigos import ARTIGOS
from generators.utils.stop_words.adjetivos import ADJETIVOS
from generators.utils.stop_words.adverbios import ADVERBIOS
from generators.utils.stop_words.conjuncoes import CONJUNCOES
from generators.utils.stop_words.contracoes import CONTRACOES
from generators.utils.stop_words.numeros import NUMEROS
from generators.utils.stop_words.preposicoes import PREPOSICOES
from generators.utils.stop_words.pronomes import PRONOMES
from generators.utils.stop_words.substantivos import SUBSTANTIVOS
from generators.utils.stop_words.conjugacoes import CONJUGACOES
from generators.utils.stop_words.verbos import VERBOS
from generators.utils.filter_tables import bad_chars


unique_terms = set()

unique_gen = [ARTIGOS, ADJETIVOS, ADVERBIOS, CONJUNCOES, CONTRACOES, VERBOS,
              NUMEROS, PREPOSICOES, PRONOMES, SUBSTANTIVOS, CONJUGACOES]

dict_merge = {}
for dt in unique_gen:
    dict_merge.update(dt)

file_ = open('machado.txt', 'r')
for line in file_.readlines():
    count += 1
    if not line.strip() or line.strip() == '\n':
        continue
    line = line.replace('\n', ' ').decode('utf-8')
    line = re.sub(r"[0-9,.;/<>:?!@#$%*()\_\\—\+\=\§\"\'\[\]]", '', line.replace('\n', ' '))
    clean_terms = [w.lower().strip() for w in line.split(' ') if len(w.lower()) > 3 and w not in dict_merge]

    for ct in clean_terms:
        # Get rid of Roman Numbers
        if len(re.findall(r"^(?:([ivxlcdm]+?)(?!.*\1))+$", ct)) != 0:
            continue
        if (len(re.findall(r"inh[ao]$", ct)) == 0
            and '-' not in ct
            and not ct.endswith('s')):
            unique_terms.add(ct)

    # clean_terms = " ".join(clean_terms)

print " . ".join(sorted(list(unique_terms)))
# print " . ".join(sorted(list(unique_terms)[:10]))
print len(unique_terms), 'terms'
print count, 'lines processed in', datetime.datetime.now() - begin, 'secs'
