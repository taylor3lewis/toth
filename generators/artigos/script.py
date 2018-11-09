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
from generators.utils.filter_tables import artigos

print artigos

for it in artigos:
    get_data = db_utils.get_nodes(it, d.ARTIGO).data()
    if len(get_data) == 0:
        print it
        db_utils.create_node(it, d.ARTIGO)
