#!/usr/bin/python
# -*- coding: utf-8 -*-

# NODE TYPES
ADVERBIO = 'Adverbio'
PREPOSICAO = 'Preposicao'
NUMERO = 'Numero'
ADJETIVO = 'Adjetivo'
SUBSTANTIVO = 'Substantivo'
VERBO = 'Verbo'
CONJUGACAO = 'Conjugacao'
PRONOME = 'Pronome'
ARTIGO = 'Artigo'
CONJUNCAO = 'Conjuncao'
CONTRACAO = 'Contracao'
# ------------------------------

# utils labels
NOT_FOUND_IN_WEB = 'not_in_web'
# ------------------------------

# Props
BINARY_SENTIMENT = 'binary_sentiment'
# ------------------------------

# NODE RELATIONSHIP
R_VERB_TENSE = "VERB_TENSE"
R_SEMANTIC_FIELD = "SEMANTICS"
R_SYNONYMOUS = "SYNONYMOUS"
R_SEMANTICS = "SEMANTICS"
R_ANTONYM = "ANTONYM"
R_ANTONYM_FIELD = "ANTONYM_FIELD"
# ----------------------------

# AUXILIARY LABELS
R_NOT_IN_WEB = "not_in_web"
R_EXPRESSION = "EXPRESSION"
# ----------------------------

VERB_TENSES = [
    'indicativo_presente',
    'indicativo_preterito_imperfeito',
    'indicativo_preterito_perfeito',
    'indicativo_preterito_mais_que_perfeito',
    'indicativo_futuro_imperfeito',
    'indicativo_futuro_perfeito_condicional',
    'conjuntivo_subjuntivo_presente',
    'conjuntivo_subjuntivo_preterito_imperfeito',
    'conjuntivo_subjuntivo_futuro',
    'imperativo_afirmativo_negativo',
    'infinitivo',
    'gerundio',
    'pessoal',
    'participio_passado'
]
