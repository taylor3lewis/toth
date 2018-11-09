# coding: utf-8
import re
from adverbios import ADVERBIOS
from artigos import ARTIGOS
from conjuncoes import CONJUNCOES
from numeros import NUMEROS
from preposicoes import PREPOSICOES
from pronomes import PRONOMES

list_categories = [ADVERBIOS, ARTIGOS, CONJUNCOES, NUMEROS, PREPOSICOES, PRONOMES]

count = 0
for category in list_categories:
    for term in category:
        result = re.search(r".+?[áàãâäéèêëíìîïóòõôöúùûüçñÁÀÃÂÄÉÈÊËÍÌÎÏÓÒÕÖÔÚÙÛÜÇ].+?", term)
        if result is not None:
            count += 1
            print '"' + term.lower() + '",',
