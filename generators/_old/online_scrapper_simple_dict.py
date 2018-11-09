#!/usr/bin/python
# -*- coding: utf-8 -*-
import regex
from generators.utils import scrapper
from generators.utils import db_utils, filter_funcs
import datetime


verb_structure = {
    '1': 'classificacao',
    '9': 'indicativo_presente',
    '10': 'indicativo_preterito_imperfeito',
    '11': 'indicativo_preterito_perfeito',
    '12': 'indicativo_preterito_mais_que_perfeito',
    '13': 'indicativo_futuro_imperfeito',
    '14': 'indicativo_futuro_perfeito_condicional',
    '25': 'conjuntivo_subjuntivo_presente',
    '26': 'conjuntivo_subjuntivo_preterito_imperfeito',
    '27': 'conjuntivo_subjuntivo_futuro',
    '28': 'imperativo_afirmativo_negativo',
    '23': 'infinitivo',
    '30': 'gerundio',
    '29': 'pessoal',
    '31': 'participio_passado'
}


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   SCRAPPY FUNCTIONS
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def scrap_general(html_full_general_scrap):
    html_full_general_scrap = html_full_general_scrap.split("name=maintext")[1]
    html_full_general_scrap = html_full_general_scrap.split("</table>")[0] + html_full_general_scrap.split("</table>")[1]
    html_full_general_scrap = filter_funcs.replace_html_entities(html_full_general_scrap)
    html_full_general_scrap = html_full_general_scrap.replace("\t", "").replace("\r", "")[1:].strip(" ")
    divisao_silabica = regex.findall(r"<p.+?Divisão silábica.+?</p>", html_full_general_scrap)
    if not divisao_silabica:
        divisao_silabica = regex.findall(r"<p.+?Divisão silábica.+?\n", html_full_general_scrap)
        divisao_silabica[0] = divisao_silabica[0].replace('\n', '')
        html_full_general_scrap = regex.sub(r"<p.+?Divisão silábica.+?\n", "", html_full_general_scrap)
    else:
        html_full_general_scrap = regex.sub(r"<p.+?Divisão silábica.+?</p>", "", html_full_general_scrap)

    while "  " in html_full_general_scrap:
        html_full_general_scrap = html_full_general_scrap.replace("  ", " ")
    while "\n\n" in html_full_general_scrap:
        html_full_general_scrap = html_full_general_scrap.replace("\n\n", "\n")
    html_full_general_scrap = regex.sub(r"<br>", ":::", html_full_general_scrap)
    html_full_general_scrap = regex.sub(r" / ", "/", html_full_general_scrap)
    html_full_general_scrap = regex.sub(r"  /  ", "/", html_full_general_scrap)
    html_full_general_scrap = html_full_general_scrap.replace(r" / ", "/")
    html_full_general_scrap = html_full_general_scrap.replace(r"  /  ", "/")
    content = regex.sub(r"</?t[dh]>", ":::", html_full_general_scrap)
    content = regex.sub(r"<.+?p>", ":::", content)
    content = regex.sub(r"<.+?>", "", content)
    temp_data = content.strip(" ").split("\n")
    return temp_data, divisao_silabica[0].replace("·", "-")


def scrap_verb(html_full_verb_scrap):
    html_full_verb_scrap = html_full_verb_scrap.split("name=maintext")[1]
    html_full_verb_scrap = html_full_verb_scrap.split("</table>")[0]
    html_full_verb_scrap = filter_funcs.replace_html_entities(html_full_verb_scrap)
    divisao_silabica = regex.findall(r"<p.+?Divisão silábica.+?</p>", html_full_verb_scrap)
    html_full_verb_scrap = html_full_verb_scrap.replace("\t", "").replace("\r", "")[1:].strip(" ")
    html_full_verb_scrap = regex.sub(r"<p.+?Divisão silábica.+?</p>", "", html_full_verb_scrap)
    participio_passado = html_full_verb_scrap.split("Particípio passado")[1]
    participio_passado = regex.sub(r"</?t[dr]>", " ", participio_passado)
    participio_passado = regex.sub(r"<.+?>", " ", participio_passado)
    participio_passado = participio_passado.replace("  /  ", "/")
    participio_passado = participio_passado.replace(" / ", "/")
    participio_passado = participio_passado.strip(" ")
    while "  " in participio_passado:
        participio_passado = participio_passado.replace("  ", " ")
    while "\n\n" in participio_passado:
        participio_passado = participio_passado.replace("\n\n", "")
    participio_passado = participio_passado.strip(" ")
    participio_passado = participio_passado.replace(" ", ":::")
    while "  " in html_full_verb_scrap:
        html_full_verb_scrap = html_full_verb_scrap.replace("  ", " ")
    while "\n\n" in html_full_verb_scrap:
        html_full_verb_scrap = html_full_verb_scrap.replace("\n\n", "\n")
    html_full_verb_scrap = regex.sub(r"<br>", ":::", html_full_verb_scrap)
    html_full_verb_scrap = regex.sub(r" / ", "/", html_full_verb_scrap)
    html_full_verb_scrap = regex.sub(r"  /  ", "/", html_full_verb_scrap)
    html_full_verb_scrap = html_full_verb_scrap.replace(r" / ", "/")
    html_full_verb_scrap = html_full_verb_scrap.replace(r"  /  ", "/")
    content = regex.sub(r"<.+?>", "", html_full_verb_scrap)
    temp_data = content.split("\n")
    clean_data = list()
    for line in temp_data:
        if "" == line.strip(" "):
            continue
        clean_data.append(line.strip(" "))
    divisao_silabica = divisao_silabica[0]
    divisao_silabica = regex.sub(r"<.+?>", "", scrapper.ascii_2_portuguese(divisao_silabica))
    return clean_data, participio_passado, divisao_silabica


def scrap_noun(html_full_noun_scrap):
    temp_data = scrap_general(html_full_noun_scrap)
    clean_data = list()
    for line in temp_data[0]:
        line = line.replace(":::", " ").replace(" : ", " ").strip(" ")
        if "" == line.strip(" ") or '' == line:
            continue
        clean_data.append(line)
    divisao_silabica = temp_data[1]
    divisao_silabica = regex.sub(r"<.+?>", "", scrapper.ascii_2_portuguese(divisao_silabica))
    return clean_data, divisao_silabica


def scrap_adjective(html_full_adjective_scrap):
    temp_data = scrap_general(html_full_adjective_scrap)
    clean_data = dict()
    for line in temp_data[0]:
        line = line.replace(":::", " ").replace(" : ", " ").strip(" ")
        if "" == line.strip(" ") or '' == line or "Masculino Feminino" in line:
            continue
        elif " - adjetivo" in line:
            clean_data["lemma"] = line.split(" ")[0]
        elif "Singular" in line:
            clean_data["sing_masc"] = line.split(" ")[1]
            clean_data["sing_femi"] = line.split(" ")[2]
        elif "Plural" in line:
            clean_data["plur_masc"] = line.split(" ")[1]
            clean_data["plur_femi"] = line.split(" ")[2]
        else:
            clean_data["more_info"] = line
    divisao_silabica = temp_data[1]
    clean_data["divisao_silabica"] = regex.sub(r"<.+?>", "", scrapper.ascii_2_portuguese(divisao_silabica))
    return clean_data


def scrap_number(html_full_number_scrap):
    temp_data = scrap_general(html_full_number_scrap)
    clean_data = dict()
    for line in temp_data[0]:
        line = line.replace(":::", " ").replace(" : ", " ").strip(" ")
        if "" == line.strip(" ") or '' == line or "Masculino Feminino" in line:
            continue
        while "  " in line:
            line = line.replace("  ", " ")
        if " - número fraccional" in line:
            clean_data["lemma"] = line.split(" ")[0]
        elif "Singular" in line:
            clean_data["sing_masc"] = line.split(" ")[1]
            clean_data["sing_femi"] = line.split(" ")[2]
        elif "Plural" in line:
            clean_data["plur_masc"] = line.split(" ")[1]
            clean_data["plur_femi"] = line.split(" ")[2]
            # else:
            #    clean_data["more_info"] = line
    divisao_silabica = temp_data[1]
    clean_data["divisao_silabica"] = regex.sub(r"<.+?>", "", scrapper.ascii_2_portuguese(divisao_silabica))
    return clean_data


def scrap_preposition(html_full_preposition_scrap):
    temp_data = scrap_general(html_full_preposition_scrap)
    clean_data = dict()
    for line in temp_data[0]:
        line = line.replace(":::", " ").replace(" : ", " ").strip(" ")
        if "" == line.strip(" ") or '' == line:
            continue
        while "  " in line:
            line = line.replace("  ", " ")
        if " - preposição" in line:
            clean_data["lemma"] = line.split(" ")[0]
            continue
        elif "Destaques" in line:
            break
        else:
            clean_data["mais_informacoes"] = line
    divisao_silabica = temp_data[1]
    clean_data["divisao_silabica"] = regex.sub(r"<.+?>", "", scrapper.ascii_2_portuguese(divisao_silabica))
    return clean_data


def scrap_adverb(html_full_adverb_scrap):
    temp_data = scrap_general(html_full_adverb_scrap)
    clean_data = dict()
    for line in temp_data[0]:
        line = line.replace(":::", " ").replace(" : ", " ").strip(" ")
        if "" == line.strip(" ") or '' == line:
            continue
        while "  " in line:
            line = line.replace("  ", " ")
        if " - advérbio" in line:
            clean_data["lemma"] = line.split(" ")[0]
            continue
        elif "Destaques" in line:
            break
        else:
            clean_data["mais_informacoes"] = line
    divisao_silabica = temp_data[1]
    clean_data["divisao_silabica"] = regex.sub(r"<.+?>", "", scrapper.ascii_2_portuguese(divisao_silabica))
    return clean_data


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   POPULATE DB FUNCTIONS
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def create_verb(html_full_verb):
    main_verb_token = regex.findall(r"<h1>.+?</h1>", html_full_verb)
    main_verb_token = regex.sub(r"<.+?>", "", main_verb_token[0])
    main_term = str(main_verb_token).split(" -")[0].strip(" ")
    verb_data = scrap_verb(html_full_verb)
    data_len = len(verb_data[0])
    divisao_silabica = verb_data[2].replace("·", "-")
    query = "CREATE (:Verbo {nid:\"" + main_term + "\", divisao_silabica:\"" + divisao_silabica + "\", "

    for vvv in range(0, data_len):
        if str(vvv) in verb_structure.keys():
            data = verb_data[0][vvv]
            if vvv == 31:
                data = scrapper.ascii_2_portuguese(verb_data[1].replace(":::", ","))
                query += verb_structure[str(vvv)] + ":[\"" + data.replace("Pessoal:::", "").replace(":::",
                                                                                                    "\",\"").replace(
                    " ", "") + "\"]"
            else:
                query += verb_structure[str(vvv)] + ":[\"" + data.replace("Pessoal:::", "").replace(":::",
                                                                                                    "\",\"").replace(
                    " ", "") + "\"], "
    query += "});"
    db_utils.execute_query(query=query)
    return query


def create_noun(html_full_noun):
    data = scrap_noun(html_full_noun)
    main_term = scrapper.ascii_2_portuguese(data[0][0].split(" - ")[0])
    gender = scrapper.ascii_2_portuguese(data[0][0].split(" - ")[1]).split(" ")[-1]
    divisao_silabica = scrapper.ascii_2_portuguese(data[1].replace("·", "-"))
    plural = data[0][-1].split(" ")[-1]
    query = "CREATE (:Substantivo {nid:\"%s\", divisao_silabica:\"%s\", genero:\"%s\", plural:\"%s\"" % (
        main_term, divisao_silabica, gender, plural
    )
    query += "});"
    db_utils.execute_query(query=query)
    return query


def create_adjective(html_full_adjective):
    data = scrap_adjective(html_full_adjective)
    query = "CREATE (:Adjetivo {nid:\"%s\", divisao_silabica:\"%s\", masculino_plural:\"%s\", feminino_plural:\"%s\", "
    if "more_info" in data.keys():
        query += "masculino_singular:\"%s\", feminino_singular:\"%s\", mais_informacoes:\"%s\"});"
        query = query % (data['lemma'], data['divisao_silabica'], data['plur_masc'], data['plur_femi'],
                         data['sing_masc'], data['sing_femi'], data['more_info'])
    else:
        query += "masculino_singular:\"%s\", feminino_singular:\"%s\"});"
        query = query % (data['lemma'], data['divisao_silabica'], data['plur_masc'], data['plur_femi'],
                         data['sing_masc'], data['sing_femi'])
    db_utils.execute_query(query=query)
    return query


def create_number(html_full_number):
    data = scrap_number(html_full_number)
    query = "CREATE (:Numero {nid:\"%s\", divisao_silabica:\"%s\", masculino_plural:\"%s\", feminino_plural:\"%s\", "
    query += "masculino_singular:\"%s\", feminino_singular:\"%s\"});"
    query = query % (data['lemma'], data['divisao_silabica'], data['plur_masc'],
                     data['plur_femi'], data['sing_masc'], data['sing_femi'])
    db_utils.execute_query(query=query)
    return query


def create_preposition(html_full_preposition):
    data = scrap_preposition(html_full_preposition)
    query = "CREATE (:Preposicao {nid:\"%s\", mais_informacoes:\"%s\", divisao_silabica:\"%s\"});"
    query = query % (data['lemma'], data['mais_informacoes'], data['divisao_silabica'])
    db_utils.execute_query(query=query)
    return query


def create_adverb(html_full_adverb):
    data = scrap_adverb(html_full_adverb)
    query = "CREATE (:Adverbio {nid:\"%s\", mais_informacoes:\"%s\", divisao_silabica:\"%s\"});"
    query = query % (data['lemma'], data['mais_informacoes'], data['divisao_silabica'])
    db_utils.execute_query(query=query)
    return query


def save_in_text_file(query, begin):
    file_ = open("simple_dict/word_queries_" + str(begin) + ".txt", "a")
    file_.write(query + "\n")
    file_.close()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   TRIGGER!
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
if '__main__' == __name__:
    begin = 150000
    threshold = 200000  # 200000
    print datetime.datetime.now()
    unique_items = dict()
    element_count = None
    for index in range(begin, threshold, 1):
        try:
            html_full = scrapper.get_html("http://www.portaldalinguaportuguesa.org/index.php?action=lemma&lemma=" + str(index))
            main_token = regex.findall(r"<h1>.+?</h1>", html_full)
            main_token = regex.sub(r"<.+?>", "", main_token[0])

            print index, main_token

            query_text = None

            flag = str(main_token).split("- ")[-1].strip(" ")
            # ERROR
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            if flag == "Search Error":
                continue

            # VERB
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            elif flag == "verbo":
                query_text = create_verb(html_full)
                # continue

            # SUBSTANTIVE
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            elif flag.split(" ")[0] == "nome":
                query_text = create_noun(html_full)
                # continue

            # ADJECTIVE
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            elif flag == "adjetivo":
                query_text = create_adjective(html_full)
                # continue

            # NUMBER
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            elif "número" in flag:
                query_text = create_number(html_full)
                # continue

            # PREPOSITION
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            elif "preposição" in flag:
                query_text = create_preposition(html_full)
                # continue

            # ADVERB
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            elif "advérbio" in flag:
                query_text = create_adverb(html_full)
                # continue

            save_in_text_file(query_text, begin)
            element_count = index
        except Exception as error:
            print str(error)
            file_error = open("simple_dict/error_report" + str(begin) + ".txt", "a")
            file_error.write(str(index) + "\n")
            file_error.close()

    print datetime.datetime.now()

    fl = open("simple_dict/elements_count.txt", "a")
    fl.write(str(element_count) + "\n")
    fl.close()
