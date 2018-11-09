#!/usr/bin/python
# -*- coding: utf-8 -*-
from generators.utils import db_utils
from generators.utils import defs as d

for node in db_utils.get_nodes_nids_by_regex(".+?[ -].+?"):
    db_utils.add_label_to_node(node.properties["nid"], d.R_EXPRESSION)
