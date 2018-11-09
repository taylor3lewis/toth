# coding: utf-8
import os
import sys
project_path = os.path.abspath(__file__).split('/')
del project_path[-1]
del project_path[-1]
del project_path[-1]
sys.path.append(os.path.join('/'.join(project_path), 'generators'))
from generators.utils import db_utils
import generators.utils.defs as d

categories = [d.CONJUGACAO]

for category in categories:
    print category
    all_ = 701741
    div = 10
    begin = 0
    for i in range(1, div+1):
        end = (all_/div)*i if i!=div else all_
        print i, begin, end
        begin = (all_ / div) * i +1

    # all_words = set()
    # result = db_utils.execute_query("MATCH (n:%s) RETURN n.nid" % category).data()

    # for node in result:
    #     w = node['n.nid']
    #     all_words.add(w)
    #
    # count = 0
    # file_ = open('all_' + category.lower() + '.txt', 'w')
    #
    # for it in all_words:
    #     if '"' in it:
    #         continue
    #     el = 'u"' + it + '": None, '
    #     count += 1
    #     file_.write(el)
    #
    # file_.close()
    #
    # print count
