#!/usr/bin/python
# -*- coding: utf-8 -*-
import regex
from generators.utils import acutes_filter
from generators.utils import scrapper
from generators.utils import db_utils
from generators.utils import defs as d
from unidecode import unidecode

target_page = r"http://www.sinonimos.com.br/"
divisor_begin = '<div class="s-wrapper">'  # <div class="s-wrapper">
breakpoint = "breakpoint"
frag = u"va"
word_stop = "valores"


def process_all_words():
    lock = True
    lock_inner = True
    reverse_alphabet = True
    letters = "abcdefghijklmnopqrstuvwxyzáàãâäéèêëíìîïóòõôöúùûüçñ".decode(encoding='utf-8')
    alphabet = [[l2 + l1 for l1 in letters] for l2 in letters]
    for letter_combination in sorted(alphabet, reverse=reverse_alphabet):
        for combination in letter_combination:
            print "+" * 50
            print combination
            if lock:
                if frag == combination:
                    lock = False
                else:
                    continue
            # -----------------------------------------------------------------------------
            result = db_utils.get_nodes_nids_by_regex("%s.+?" % combination)
            # -----------------------------------------------------------------------------
            if result:
                # Sort Result Alphabetically ----------------------
                for term in sorted(result, key=lambda k: k['nid']):
                    if lock_inner:
                        if term['nid'] == word_stop:
                            lock_inner = False
                        else:
                            continue
                    # --------------------------------------------
                    print len(result), term["nid"], "-" * 50
                    try:
                        if reverse_alphabet:
                            open(breakpoint + '_r.txt', 'w').write(str(combination + ":" + term['nid']))
                        else:
                            open(breakpoint + '.txt', 'w').write(str(combination + ":" + term['nid']))
                    except:
                        pass
                    # --------------------------------------------
                    # process lemma
                    if process_semantic_relationships(term['nid']) is None:
                        db_utils.add_label(term['nid'], d.NOT_FOUND_IN_WEB)
                        print 'unable to get page:', target_page + unidecode(unicode(term['nid']))
                        pass
                    else:
                        print term['nid'], 'already done'
                    continue


def process_semantic_relationships(word):
    try:
        page = scrapper.get_html(target_page + unidecode(unicode(word)), print_erros=False)
        if page is None:
            return None
        no_script = scrapper.remove_tag_and_content(html=page, tag='script')
        meanings = no_script.split(divisor_begin)
        del meanings[0]
        meanings[-1] = meanings[-1].split("</p></div>")[0]

        for i, it in enumerate(meanings):
            field_of_lemmas = regex.findall(r"<a.+?>.+?</a>", it)
            field_of_lemmas = [l.replace("</a>", "") for l in field_of_lemmas]
            field_of_lemmas = [regex.sub("<a.+?>", "", l) for l in field_of_lemmas]
            for lemma in field_of_lemmas:
                if i == 0:
                    db_utils.create_semantic_relationship(lemma.lower(),
                                                          word.lower(),
                                                          d.R_SEMANTIC_FIELD)
                for current_lemma in field_of_lemmas:
                    if current_lemma != lemma:
                        db_utils.create_semantic_relationship(lemma.lower(),
                                                              current_lemma.lower(),
                                                              d.R_SEMANTIC_FIELD)
    except Exception as error:
        print error, target_page + unidecode(unicode(word))


if __name__ == '__main__':
    process_all_words()
