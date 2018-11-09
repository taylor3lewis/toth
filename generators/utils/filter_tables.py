# coding: utf-8
import re

CLASSES_MORFOLOGICAS = [
    "substantivo",  # 1
    "artigo",  # 2
    "adjetivo",  # 3
    "numeral",  # 4
    "pronome",  # 5
    "verbo",  # 6
    "advérbio",  # 7
    "preposição",  # 8
    "conjunção",  # 9
    "interjeição"  # 10
]

bad_chars = re.compile(r"[^a-záàãâäéèêëíìîïóòõôöúùûüçñÁÀÃÂÄÉÈÊËÍÌÎÏÓÒÕÖÔÚÙÛÜÇ\s\-]", re.UNICODE)
bad_chars_utf8 = re.compile(r"[^a-záàãâäéèêëíìîïóòõôöúùûüçñÁÀÃÂÄÉÈÊËÍÌÎÏÓÒÕÖÔÚÙÛÜÇ\s\-]")
parse_chars = re.compile(r"[^a-záàãâäéèêëíìîïóòõôöúùûüçñÁÀÃÂÄÉÈÊËÍÌÎÏÓÒÕÖÔÚÙÛÜÇ\s]", re.UNICODE)
valid_chars = re.compile(r"[a-záàãâäéèêëíìîïóòõôöúùûüçñÁÀÃÂÄÉÈÊËÍÌÎÏÓÒÕÖÔÚÙÛÜÇ]", re.UNICODE)

breakable_sentence_chars = re.compile(r"[\s\n\t\r\.,;]", re.UNICODE)

HTML_ENTITIES_TABLE_CODES = [
    ("&#160;", "&nbsp;", " "), ("&#161;", "&iexcl;", "¡"), ("&#162;", "&cent;", "¢"),
    ("&#163;", "&pound;", "£"), ("&#164;", "&curren;", "¤"), ("&#165;", "&yen;", "¥"),
    ("&#166;", "&brvbar;", "¦"), ("&#167;", "&sect;", "§"), ("&#168;", "&uml;", "¨"),
    ("&#169;", "&copy;", "©"), ("&#170;", "&ordf;", "ª"), ("&#171;", "&laquo;", "«"),
    ("&#172;", "&not;", "¬"), ("&#173;", "&shy;", " "), ("&#174;", "&reg;", "®"),
    ("&#175;", "&macr;", "¯"), ("&#176;", "&deg;", "°"), ("&#177;", "&plusmn;", "±"),
    ("&#178;", "&sup2;", "²"), ("&#179;", "&sup3;", "³"), ("&#180;", "&acute;", "´"),
    ("&#181;", "&micro;", "µ"), ("&#182;", "&para;", "¶"), ("&#183;", "&middot;", "·"),
    ("&#184;", "&cedil;", "¸"), ("&#185;", "&sup1;", "¹"), ("&#186;", "&ordm;", "º"),
    ("&#187;", "&raquo;", "»"), ("&#188;", "&frac14;", "¼"), ("&#189;", "&frac12;", "½"),
    ("&#190;", "&frac34;", "¾"), ("&#191;", "&iquest;", "¿"), ("&#192;", "&Agrave;", "À"),
    ("&#193;", "&Aacute;", "Á"), ("&#194;", "&Acirc;", "Â"), ("&#195;", "&Atilde;", "Ã"),
    ("&#196;", "&Auml;", "Ä"), ("&#197;", "&Aring;", "Å"), ("&#198;", "&AElig;", "Æ"),
    ("&#199;", "&Ccedil;", "Ç"), ("&#200;", "&Egrave;", "È"), ("&#201;", "&Eacute;", "É"),
    ("&#202;", "&Ecirc;", "Ê"), ("&#203;", "&Euml;", "Ë"), ("&#204;", "&Igrave;", "Ì"),
    ("&#205;", "&Iacute;", "Í"), ("&#206;", "&Icirc;", "Î"), ("&#207;", "&Iuml;", "Ï"),
    ("&#208;", "&ETH;", "Ð"), ("&#209;", "&Ntilde;", "Ñ"), ("&#210;", "&Ograve;", "Ò"),
    ("&#211;", "&Oacute;", "Ó"), ("&#212;", "&Ocirc;", "Ô"), ("&#213;", "&Otilde;", "Õ"),
    ("&#214;", "&Ouml;", "Ö"), ("&#215;", "&times;", "×"), ("&#216;", "&Oslash;", "Ø"),
    ("&#217;", "&Ugrave;", "Ù"), ("&#218;", "&Uacute;", "Ú"), ("&#219;", "&Ucirc;", "Û"),
    ("&#220;", "&Uuml;", "Ü"), ("&#221;", "&Yacute;", "Ý"), ("&#222;", "&THORN;", "Þ"),
    ("&#223;", "&szlig;", "ß"), ("&#224;", "&agrave;", "à"), ("&#225;", "&aacute;", "á"),
    ("&#226;", "&acirc;", "â"), ("&#227;", "&atilde;", "ã"), ("&#228;", "&auml;", "ä"),
    ("&#229;", "&aring;", "å"), ("&#230;", "&aelig;", "æ"), ("&#231;", "&ccedil;", "ç"),
    ("&#232;", "&egrave;", "è"), ("&#233;", "&eacute;", "é"), ("&#234;", "&ecirc;", "ê"),
    ("&#235;", "&euml;", "ë"), ("&#236;", "&igrave;", "ì"), ("&#237;", "&iacute;", "í"),
    ("&#238;", "&icirc;", "î"), ("&#239;", "&iuml;", "ï"), ("&#240;", "&eth;", "ð"),
    ("&#241;", "&ntilde;", "ñ"), ("&#242;", "&ograve;", "ò"), ("&#243;", "&oacute;", "ó"),
    ("&#244;", "&ocirc;", "ô"), ("&#245;", "&otilde;", "õ"), ("&#246;", "&ouml;", "ö"),
    ("&#247;", "&divide;", "÷"), ("&#248;", "&oslash;", "ø"), ("&#249;", "&ugrave;", "ù"),
    ("&#250;", "&uacute;", "ú"), ("&#251;", "&ucirc;", "û"), ("&#252;", "&uuml;", "ü"),
    ("&#253;", "&yacute;", "ý"), ("&#254;", "&thorn;", "þ"), ("&#255;", "&yuml;", "ÿ"),
    ("&#338;", None, "Œ"), ("&#339;", None, "œ"), ("&#352;", None, "Š"), ("&#353;", None, "š"),
    ("&#376;", None, "Ÿ"), ("&#402;", None, "ƒ"), ("&#8211;", None, "–"), ("&#8212;", None, "—"),
    ("&#8216;", None, "‘"), ("&#8217;", None, "’"), ("&#8218;", None, "‚"), ("&#8220;", None, "“"),
    ("&#8221;", None, "”"), ("&#8222;", None, "„"), ("&#8224;", None, "†"), ("&#8225;", None, "‡"),
    ("&#8226;", None, "•"), ("&#8230;", None, "…"), ("&#8240;", None, "‰"), ("&#8364;", "&euro;", "€"),
    ("&#8482;", None, "™")]

CHARS = ["", "¡", "¢", "£", "¤", "¥", "¦", "§", "¨", "©", "ª", "«", "¬", "", "®", "¯", "°", "±", "²", "³", "´", "µ",
         "¶", "·", "¸", "¹", "º", "»", "¼", "½", "¾", "¿", "À", "Á", "Â", "Ã", "Ä", "Å", "Æ", "Ç", "È", "É", "Ê", "Ë",
         "Ì", "Í", "Î", "Ï", "Ð", "Ñ", "Ò", "Ó", "Ô", "Õ", "Ö", "×", "Ø", "Ù", "Ú", "Û", "Ü", "Ý", "Þ", "ß", "à", "á",
         "â", "ã", "ä", "å", "æ", "ç", "è", "é", "ê", "ë", "ì", "í", "î", "ï", "ð", "ñ", "ò", "ó", "ô", "õ", "ö", "÷",
         "ø", "ù", "ú", "û", "ü", "ý", "þ", "ÿ", "Œ", "œ", "Š", "š", "Ÿ", "ƒ", "–", "—", "‘", "’", "‚", "“", "”", "„",
         "†", "‡", "•", "…", "‰", "€", "™", ""]

NUMBS = ["&#160;", "&#161;", "&#162;", "&#163;", "&#164;", "&#165;", "&#166;", "&#167;", "&#168;", "&#169;", "&#170;",
         "&#171;", "&#172;", "&#173;", "&#174;", "&#175;", "&#176;", "&#177;", "&#178;", "&#179;", "&#180;", "&#181;",
         "&#182;", "&#183;", "&#184;", "&#185;", "&#186;", "&#187;", "&#188;", "&#189;", "&#190;", "&#191;", "&#192;",
         "&#193;", "&#194;", "&#195;", "&#196;", "&#197;", "&#198;", "&#199;", "&#200;", "&#201;", "&#202;", "&#203;",
         "&#204;", "&#205;", "&#206;", "&#207;", "&#208;", "&#209;", "&#210;", "&#211;", "&#212;", "&#213;", "&#214;",
         "&#215;", "&#216;", "&#217;", "&#218;", "&#219;", "&#220;", "&#221;", "&#222;", "&#223;", "&#224;", "&#225;",
         "&#226;", "&#227;", "&#228;", "&#229;", "&#230;", "&#231;", "&#232;", "&#233;", "&#234;", "&#235;", "&#236;",
         "&#237;", "&#238;", "&#239;", "&#240;", "&#241;", "&#242;", "&#243;", "&#244;", "&#245;", "&#246;", "&#247;",
         "&#248;", "&#249;", "&#250;", "&#251;", "&#252;", "&#253;", "&#254;", "&#255;", "&#338;", "&#339;", "&#352;",
         "&#353;", "&#376;", "&#402;", "&#8211;", "&#8212;", "&#8216;", "&#8217;", "&#8218;", "&#8220;", "&#8221;",
         "&#8222;", "&#8224;", "&#8225;", "&#8226;", "&#8230;", "&#8240;", "&#8364;", "&#8482;"]

ENTIT = ["&nbsp;", "&iexcl;", "&cent;", "&pound;", "&curren;", "&yen;", "&brvbar;", "&sect;", "&uml;", "&copy;",
         "&ordf;", "&laquo;", "&not;", "&shy;", "&reg;", "&macr;", "&deg;", "&plusmn;", "&sup2;", "&sup3;", "&acute;",
         "&micro;", "&para;", "&middot;", "&cedil;", "&sup1;", "&ordm;", "&raquo;", "&frac14;", "&frac12;", "&frac34;",
         "&iquest;", "&Agrave;", "&Aacute;", "&Acirc;", "&Atilde;", "&Auml;", "&Aring;", "&AElig;", "&Ccedil;",
         "&Egrave;", "&Eacute;", "&Ecirc;", "&Euml;", "&Igrave;", "&Iacute;", "&Icirc;", "&Iuml;", "&ETH;", "&Ntilde;",
         "&Ograve;", "&Oacute;", "&Ocirc;", "&Otilde;", "&Ouml;", "&times;", "&Oslash;", "&Ugrave;", "&Uacute;",
         "&Ucirc;", "&Uuml;", "&Yacute;", "&THORN;", "&szlig;", "&agrave;", "&aacute;", "&acirc;", "&atilde;", "&auml;",
         "&aring;", "&aelig;", "&ccedil;", "&egrave;", "&eacute;", "&ecirc;", "&euml;", "&igrave;", "&iacute;",
         "&icirc;", "&iuml;", "&eth;", "&ntilde;", "&ograve;", "&oacute;", "&ocirc;", "&otilde;", "&ouml;", "&divide;",
         "&oslash;", "&ugrave;", "&uacute;", "&ucirc;", "&uuml;", "&yacute;", "&thorn;", "&yuml;", "", "", "", "", "",
         "", "", "", "", "", "", "", "", "", "", "", "", "", "", "&euro;", ""]

preposicoes = ['a', 'afora', 'ante', 'ao', 'aonde', 'aos', 'após', 'até', 'com', 'conforme', 'contra', 'da',
               'dali', 'daquelas', 'daqueles', 'daqui', 'daquilo', 'das', 'daí', 'de', 'delas', 'deles',
               'desde', 'dessas', 'desses', 'destas', 'destes', 'disso', 'disto', 'do', 'dos', 'doutras',
               'doutros', 'dum', 'duma', 'dumas', 'duns', 'durante', 'em', 'entre', 'excepto', 'exceto',
               'fora', 'malgrado', 'mediante', 'menos', 'na', 'naquelas', 'naqueles', 'naquilo', 'nas', 'nesses',
               'nestas', 'nestes', 'nisso', 'nisto', 'no', 'nos', 'num', 'numa', 'numas', 'nuns', 'para', 'pela',
               'pelas', 'pelo', 'pelos', 'perante', 'por', 'salvo', 'segundo', 'sem', 'sob', 'sobre', 'trás', 'à',
               'àquelas', 'àqueles', 'àquilo', 'às']

artigos = ['o', 'os', 'a', 'as', 'um', 'uns', 'uma', 'umas']

pronomes = ['me', 'te', 'o', 'a', 'lhe', 'se', 'nos', 'vos', 'os', 'as', 'lhes', 'eu', 'tu', 'ele', 'ela', 'nós', 'vós',
            'ele', 'ela', 'meu', 'minha', 'nosso', 'nossa', 'teu', 'tua', 'vosso', 'vossa', 'seu', 'sua', 'dele',
            'dela', 'meus', 'minhas', 'nossos', 'nossas', 'teus', 'tuas', 'vossos', 'vossas', 'seus', 'suas', 'deles',
            'delas', 'algum', 'alguns', 'alguma', 'algumas', 'nenhum', 'nenhuns', 'nenhuma', 'nenhumas', 'todo',
            'todos', 'toda', 'todas', 'muito', 'muitos', 'muita', 'muitas', 'pouco', 'poucos', 'pouca', 'poucas',
            'tanto', 'tantos', 'tanta', 'tantas', 'certo', 'certos', 'certa', 'certas', 'vário', 'vários', 'vária',
            'várias', 'outro', 'outros', 'outra', 'outras', 'certo', 'certos', 'certa', 'certas', 'quanto', 'quantos',
            'quanta', 'quantas', 'tal', 'tals', 'tais', 'qual', 'quals', 'quais', 'qualquer', 'quaisquer',
            'quaisqueres', 'isso', 'esse', 'isto', 'este', 'você']

adverbios = ['aqui', 'antes', 'dentro', 'ali', 'adiante', 'fora', 'acolá', 'atrás', 'além', 'lá', 'detrás', 'aquém',
             'cá', 'acima', 'onde', 'perto', 'aí', 'abaixo', 'aonde', 'longe', 'debaixo', 'algures', 'defronte',
             'nenhures', 'adentro', 'afora', 'alhures', 'nenhures', 'aquém', 'embaixo', 'externamente', 'distância',
             'distância', 'longe', 'perto', 'cima', 'direita', 'esquerda', 'lado', 'volta', 'hoje', 'logo', 'primeiro',
             'ontem', 'tarde', 'outrora', 'amanhã', 'cedo', 'dantes', 'depois', 'ainda', 'antigamente', 'antes',
             'doravante', 'nunca', 'então', 'ora', 'jamais', 'agora', 'sempre', 'já', 'enfim', 'afinal', 'amiúde',
             'breve', 'constantemente', 'entrementes', 'imediatamente', 'primeiramente', 'provisoriamente',
             'sucessivamente', 'vezes', 'tarde', 'noite', 'manhã', 'repente', 'vez', 'quando', 'quando', 'qualquer',
             'tempos', 'breve', 'assim', 'adrede', 'melhor', 'pior', 'depressa', 'acinte', 'debalde', 'devagar', 'toa',
             'desse', 'dessa', 'sim', 'certamente', 'realmente', 'decerto', 'efetivamente', 'certo', 'decididamente',
             'deveras', 'indubitavelmente', 'não', 'nem', 'nunca', 'jamais', 'algum', 'nenhuma', 'tampouco', 'nenhum',
             'porventura', 'possivelmente', 'provavelmente', 'quiçá', 'talvez', 'casualmente', 'muito', 'demais',
             'pouco', 'tão', 'bastante', 'mais', 'menos', 'demasiado', 'quanto', 'quão', 'tanto', 'assaz', 'que',
             'quão', 'tudo', 'nada', 'todo', 'quase', 'completo', 'extremamente', 'intensamente', 'grandemente',
             'apenas', 'exclusivamente', 'senão', 'somente', 'simplesmente', 'só', 'unicamente', 'ainda', 'até',
             'mesmo', 'inclusivamente', 'também', 'depois', 'primeiramente', 'ultimamente'
             ]

entidades_html = ['&#32;', '&#33;', '&#34;', '&#35;', '&#36;', '&#37;', '&#38;', '&#39;', '&#40;',
                  '&#41;', '&#42;', '&#43;', '&#44;', '&#45;', '&#46;', '&#47;', '&quot;', '&amp;',
                  '&#48;', '&#49;', '&#50;', '&#51;', '&#52;', '&#53;', '&#54;', '&#55;', '&#56;',
                  '&#57;', '&#58;', '&#59;', '&#60;', '&#61;', '&#62;', '&#63;', '&lt;', '&gt;',
                  '&#64;', '&#65;', '&#66;', '&#67;', '&#68;', '&#69;', '&#70;', '&#71;', '&#72;',
                  '&#73;', '&#74;', '&#75;', '&#76;', '&#77;', '&#78;', '&#79;', '&#80;', '&#81;',
                  '&#82;', '&#83;', '&#84;', '&#85;', '&#86;', '&#87;', '&#88;', '&#89;', '&#90;',
                  '&#91;', '&#92;', '&#93;', '&#94;', '&#95;', '&#96;', '&#97;', '&#98;', '&#99;',
                  '&#100;', '&#101;', '&#102;', '&#103;', '&#104;', '&#105;', '&#106;', '&#107;',
                  '&#108;', '&#109;', '&#110;', '&#111;', '&#112;', '&#113;', '&#114;', '&#115;',
                  '&#116;', '&#117;', '&#118;', '&#119;', '&#120;', '&#121;', '&#122;', '&#123;',
                  '&#124;', '&#125;', '&#126;', '&#160;', '&#161;', '&#162;', '&#163;', '&#164;',
                  '&#165;', '&#166;', '&#167;', '&#168;', '&#169;', '&#170;', '&#171;', '&#172;',
                  '&#173;', '&#174;', '&#175;', '&nbsp;', '&iexcl;', '&cent;', '&pound;', '&curren;',
                  '&yen;', '&brvbar;', '&sect;', '&uml;', '&copy;', '&ordf;', '&laquo;', '&not;',
                  '&shy;', '&reg;', '&macr;', '&#176;', '&#177;', '&#178;', '&#179;', '&#180;',
                  '&#181;', '&#182;', '&#183;', '&#184;', '&#185;', '&#186;', '&#187;', '&#188;',
                  '&#189;', '&#190;', '&#191;', '&deg;', '&plusmn;', '&sup2;', '&sup3;', '&micro;',
                  '&para;', '&middot;', '&sup1;', '&ordm;', '&raquo;', '&frac14;', '&frac12;',
                  '&frac34;', '&iquest;', '&#192;', '&#193;', '&#194;', '&#195;', '&#196;', '&#197;',
                  '&#198;', '&#199;', '&#200;', '&#201;', '&#202;', '&#203;', '&#204;', '&#205;',
                  '&#206;', '&#207;', '&Atilde;', '&Auml;', '&Aring;', '&AElig;', '&Euml;', '&Iuml;',
                  '&#208;', '&#209;', '&#210;', '&#211;', '&#212;', '&#213;', '&#214;', '&#215;',
                  '&#216;', '&#217;', '&#218;', '&#219;', '&#220;', '&#221;', '&#222;', '&#223;',
                  '&ETH;', '&Ntilde;', '&Otilde;', '&Ouml;', '&times;', '&Oslash;', '&Uuml;',
                  '&THORN;', '&szlig;', '&#224;', '&#225;', '&#226;', '&#227;', '&#228;', '&#229;',
                  '&#230;', '&#231;', '&#232;', '&#233;', '&#234;', '&#235;', '&#236;', '&#237;',
                  '&#238;', '&#239;', '&auml;', '&aring;', '&aelig;', '&euml;', '&iuml;', '&#240;',
                  '&#241;', '&#242;', '&#243;', '&#244;', '&#245;', '&#246;', '&#247;', '&#248;',
                  '&#249;', '&#250;', '&#251;', '&#252;', '&#253;', '&#254;', '&#255;', '&eth;',
                  '&ntilde;', '&otilde;', '&ouml;', '&divide;', '&oslash;', '&uuml;', '&thorn;',
                  '&yuml;', '&#338;', '&#339;', '&#352;', '&#353;', '&#376;', '&#402;', '&#8211;',
                  '&#8212;', '&#8216;', '&#8217;', '&#8218;', '&#8220;', '&#8221;', '&#8222;',
                  '&#8224;', '&#8225;', '&#8226;', '&#8230;', '&#8240;', '&#8364;', '&#8482;', '&euro;'
                  ]
