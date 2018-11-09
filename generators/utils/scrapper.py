#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import re
import filter_funcs

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) '
user_agent += 'Chrome/23.0.1271.64 Safari/537.11'
mozilla5_0 = {'User-Agent': user_agent}


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   UTILS FUNCTIONS
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def ascii_2_portuguese(text):
    text = text.decode('iso-8859-1')
    text = text.encode('latin1')
    return text


def get_html(page=None, print_erros=True):
    if page is not None:
        try:
            request = urllib2.Request(page, headers=mozilla5_0)
            response = urllib2.urlopen(request)
            encoding = response.headers['content-type'].split('charset=')[-1]
            content = response.read()
            u_content = unicode(content, encoding).encode('utf-8')
            html_page = re.sub(ur'[^\p{Latin}]', u'', u_content, re.UNICODE)
            return html_page
        except urllib2.HTTPError as err:
            if err.getcode() == 404:
                return None
        except Exception as general_error:
            if print_erros:
                print 'Attempt ONE:', str(general_error)
            try:
                request = urllib2.Request(page, headers=mozilla5_0)
                response = urllib2.urlopen(request)
                content = response.read()
                u_content = content.decode('iso-8859-1').encode('utf-8')
                html_page = re.sub(ur'[^\p{Latin}]', u'', u_content, re.UNICODE)
                return html_page
            except Exception as err:
                if print_erros:
                    print 'Attempt TWO:', str(err)
                raise err
    else:
        print 'get_html(page="http://www.example.com")'


def scrap_general(html_full_general_scrap):
    while "  " in html_full_general_scrap:
        html_full_general_scrap = html_full_general_scrap.replace("  ", " ")
    while "\n\n" in html_full_general_scrap:
        html_full_general_scrap = html_full_general_scrap.replace("\n\n", "\n")

    html_full_general_scrap = filter_funcs.replace_html_entities(html_full_general_scrap)
    # html_full_general_scrap = html_full_general_scrap.replace("\t", "").replace("\r", "").replace("\n", "").strip(" ")
    html_full_general_scrap = re.sub(r"<br>", " ", html_full_general_scrap)
    html_full_general_scrap = re.sub(r" / ", "/", html_full_general_scrap)
    html_full_general_scrap = re.sub(r"  /  ", "/", html_full_general_scrap)
    html_full_general_scrap = html_full_general_scrap.replace("\n", " ")
    html_full_general_scrap = html_full_general_scrap.replace("'", "\"")
    html_full_general_scrap = html_full_general_scrap.replace(" / ", "/")
    html_full_general_scrap = html_full_general_scrap.replace("  /  ", "/")
    return html_full_general_scrap


def remove_all_tags(content):
    return re.sub(r"<.+?>", "", content)


def remove_tag_and_content(html=None, tag=None):
    if tag is not None and html is not None:
        html = str(html)
        tag = str(tag).replace('<', '').replace('>', '')
        tag_end = '</' + tag + '>'
        tag = '<' + tag
        buffer_dynamic = ''
        buffer_safe = ''
        in_tag = False
        for char in html:
            buffer_dynamic += char
            if tag in buffer_dynamic and not in_tag:
                in_tag = True
                buffer_safe += buffer_dynamic.replace(tag, '') + ' '
                buffer_dynamic = ''
            if tag_end in buffer_dynamic and in_tag:
                buffer_dynamic = ''
                in_tag = False
        buffer_safe += buffer_dynamic
        return scrap_general(buffer_safe)
    else:
        print "Function -> remove_tag_and_content(), says: Hey, Give me params!"
