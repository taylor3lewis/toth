#!/usr/bin/python
# -*- coding: utf-8 -*-
from glob import glob
from unidecode import unidecode
from generators.utils import scrapper
import regex
from generators.utils import db_utils

target_page = r"http://www.sinonimos.com.br/"
divisor_begin = '<div class="s-wrapper">'  # <div class="s-wrapper">


if __name__ == '__main__':
    # file_ = 'simple_dict_outputs/word_queries/file_query1.txt'
    for file_ in glob('simple_dict_outputs/word_queries/*'):
        open('file_prog.txt', 'a').write(file_ + "\n")
        queries = open(file_, 'r')
        for query in queries.readlines():
                word = query.replace('\n', '').split('"')[1]
                if 'crebro' in word:
                    print word, unidecode(unicode(word.decode('utf-8')))
                if regex.match(r"[áàãâäéèêëíìîïóòõôöúùûüçñÁÀÃÂÄÉÈÊËÍÌÎÏÓÒÕÖÔÚÙÛÜÇ]", word):
                    if 'cérebro' in word:
                        print word, unidecode(unicode(word.decode('utf-8')))
                continue
                open('word_prog.txt', 'a').write(word + "\n")
                try:
                    page = scrapper.get_html(target_page + unidecode(unicode(word.decode('utf-8'))), print_erros=False)
                    if page is None:
                        print 'unable to get page:', target_page + unidecode(unicode(word.decode('utf-8')))
                        continue
                    page_clean = scrapper.scrap_general(page)
                    no_script = scrapper.remove_tag_and_content(html=page, tag='script')
                    meanings = no_script.split(divisor_begin)
                    del meanings[0]
                    meanings[-1] = meanings[-1].split("</p></div>")[0]

                    synonyms = set()
                    for piece in meanings:
                        piece = scrapper.remove_all_tags(piece)
                        piece = regex.findall(r"[a-zA-Z,]", piece.split(':')[-1])
                        # piece.split(':')[-1].replace('.', '')
                        temp_synonyms = ''.join(piece).split(',')

                        for t_s in temp_synonyms:
                            synonyms.add(t_s)

                        for synonym in synonyms:
                            db_utils.create_relationship_synonym(word, synonym)
                            print "relationship created (%s)--[:synonym]-->(%s)" % (word, synonym)
                            file_temp = open("script.stop.txt", "w")
                            file_temp.write("relationship created (%s)--[:synonym]-->(%s)" % (word, synonym))
                            file_temp.close()

                except Exception as error:
                    print error, target_page + unidecode(unicode(word.decode('utf-8')))

        queries.close()
