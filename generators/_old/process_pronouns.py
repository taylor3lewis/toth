#!/usr/bin/python
# -*- coding: utf-8 -*-
from generators.utils import db_utils
from generators.utils import defs as d


def pessoais():
    position = 0
    file_ = open('pronomes/pessoais.txt', 'r')
    for line in file_.readlines():
        line = line.replace('\n', '').lstrip(' ').rstrip(' ')
        if '>' in line:
            position += 1
            continue
        if position == 0:
            db_utils.create_node(node_id=line, node_type=d.PRONOME)
        elif position == 1:
            db_utils.create_node(node_id=line, node_type=d.PRONOME,
                                 additional_params={'subcategoria': 'oblíquos átonos'})
        elif position == 2:
            db_utils.create_node(node_id=line, node_type=d.PRONOME,
                                 additional_params={'subcategoria': 'oblíquos tônicos'})
        elif position == 3:
            db_utils.create_node(node_id=line, node_type=d.PRONOME,
                                 additional_params={'subcategoria': 'tratamento'})
    file_.close()


def demonstrativos():
    file_ = open('pronomes/demonstrativos.txt', 'r')
    for line in file_.readlines():
        line = line.replace('\n', '').lstrip(' ').rstrip(' ')
        db_utils.create_node(node_id=line, node_type=d.PRONOME,
                             additional_params={'subcategoria': 'demonstrativo'})
    file_.close()


def indefinidos():
    file_ = open('pronomes/indefinidos.txt', 'r')
    for line in file_.readlines():
        line = line.replace('\n', '').lstrip(' ').rstrip(' ')
        db_utils.create_node(node_id=line, node_type=d.PRONOME,
                             additional_params={'subcategoria': 'indefinido'})
    file_.close()


def interrogativos():
    file_ = open('pronomes/interrogativos.txt', 'r')
    for line in file_.readlines():
        line = line.replace('\n', '').lstrip(' ').rstrip(' ')
        db_utils.create_node(node_id=line, node_type=d.PRONOME,
                             additional_params={'subcategoria': 'interrogativo'})
    file_.close()


def possessivos():
    file_ = open('pronomes/possessivos.txt', 'r')
    for line in file_.readlines():
        line = line.replace('\n', '').lstrip(' ').rstrip(' ')
        db_utils.create_node(node_id=line, node_type=d.PRONOME,
                             additional_params={'subcategoria': 'possessivo'})
    file_.close()


def relativos():
    file_ = open('pronomes/relativos.txt', 'r')
    for line in file_.readlines():
        line = line.replace('\n', '').lstrip(' ').rstrip(' ')
        db_utils.create_node(node_id=line, node_type=d.PRONOME,
                             additional_params={'subcategoria': 'relativo'})
    file_.close()


if __name__ == '__main__':
    pessoais()
    demonstrativos()
    indefinidos()
    interrogativos()
    possessivos()
    relativos()
