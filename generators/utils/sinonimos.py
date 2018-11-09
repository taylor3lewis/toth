# -*- coding: utf-8 -*-
from py2neo import authenticate, Graph
import unidecode


HOST = "localhost:7474"
USER = "neo4j"
PASS = "hSo3Fl6rt6"
GRAPH = "http://localhost:7474/db/data/"


def execute_query(query):
    """
    :param query:
    :return:
    """
    try:
        authenticate(HOST, USER, PASS)
        graph = Graph(GRAPH)
        return graph.run(query)
    except Exception as error:
        print str(error)


def database_connection_test():
    """
    :return:
    """
    try:
        return execute_query("MATCH (n) RETURN n")
    except Exception as err:
        print unidecode.unidecode(err.message)


def create_synonymous(nid, synonymous):
    """
    :param nid:
    :param synonymous:
    :return:
    """
    if nid == '' or synonymous == []:
        print 'please give me params...'
    try:
        synonymous_formatted = list()
        for sn in synonymous:
            synonymous_formatted.append("\"" + sn + "\"")
        synonymous_formatted = ','.join(synonymous_formatted)
        query = "CREATE (:Word {nid:\"" + nid.decode('utf-8') + "\", "
        query += "synonymous:[" + synonymous_formatted.decode('utf-8') + "]});"
        return execute_query(query)
    except Exception as err:
        print unidecode.unidecode(err.message)


def search_in_synonymous(string):
    """
    :param string:
    :return:
    """
    query = "MATCH (n) WHERE ANY(single_syn IN n.synonymous WHERE single_syn =~ '.*%s.*') RETURN n;" % string
    return execute_query(query=query)


def search_word(string=None):
    """
    :param string:
    :return:
    """
    query = "MATCH (n) WHERE n.nid =~ '.*%s.*' RETURN n;" % string.upper()
    return execute_query(query=query)
