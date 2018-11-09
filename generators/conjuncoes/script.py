# coding: utf-8
import os
import sys
project_path = os.path.abspath(__file__).split('/')
del project_path[-1]
del project_path[-1]
del project_path[-1]
sys.path.append(os.path.join('/'.join(project_path), 'generators'))
from generators.utils import db_utils
from generators.utils import defs as d

file_ = open('conj.txt', 'r')
for line in file_.readlines():
    line = line.strip()
    w = line.strip().strip('\n')
    if line.strip() and line.strip() != '\n' and ' ' not in line:
        get_data = db_utils.get_nodes(w, d.CONJUNCAO).data()
        if len(get_data) == 0:
            print w
            db_utils.create_node(w, d.CONJUNCAO)
