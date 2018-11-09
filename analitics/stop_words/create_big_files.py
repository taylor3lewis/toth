# coding: utf-8
file_stream = open('all_verbo.txt', 'r')
# file_stream = open('all_artigo.txt', 'r')
content = file_stream.read()
file_stream.close()

file_write = open('verbos.py', 'w')
file_write.write("# coding: utf-8\n")
file_write.write("VERBOS = {" + content[:-2] + "}")
file_write.close()
