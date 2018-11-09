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

TYPE = d.CONTRACAO


def node(w):
    get_data = db_utils.get_nodes(w, TYPE).data()
    if len(get_data) == 0:
        db_utils.create_node(w, TYPE)


file_ = open('contr.txt', 'r')
for line in file_.readlines():
    line = line.strip()
    if '\n' in line:
        line = line.strip().strip('\n').strip()

    if line and line.strip() != '\n':
        wd = line.split('–')[-1].strip()
        node(wd.split('(')[0].strip())

        if '(' in wd:
            wd = wd.split('(')[0] + 's'
            node(wd.strip())
