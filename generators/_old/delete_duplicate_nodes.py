from generators.utils import db_utils
from glob import glob


if __name__ == '__main__':
    # file_ = 'simple_dict_outputs/word_queries/file_query1.txt'
    for file_ in glob('simple_dict_outputs/word_queries/*'):
        print 'file:', file_
        queries = open(file_, 'r')
        for line in queries.readlines():
            word = line.replace('\n', '').split('"')[1]
            gram = line.replace('\n', '').split(':')[1].split(' ')[0]
            query = """MATCH (n:%s {nid: "%s"}) WITH n SKIP 1 DELETE n;""" % (gram, word)
            # query = """MATCH (n:%s {nid: "%s"}) RETURN n;""" % (gram, word)
            result = db_utils.execute_query(query).evaluate()
            if result:
                print result
