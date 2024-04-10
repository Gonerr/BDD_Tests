from behave import given, when, then
from paspailleur import pattern_structures as PS
from paspailleur.pattern_structures.nlp_ps import SynonymPS, AntonymPS
import unittest


# Предварительная обработка данных для получения всех синонимов слов
    def preprocess_with_synonyms(data):
        ps = SynonymPS(n_synonyms=5)
        synonyms = set()
        for word in data.split():
            synonyms |= ps.get_synonyms(word)
        return synonyms

    @given(u'два описания {d1} и {d2} с синонимами слов')
    def step_impl(context, d1, d2):
        print(u'Шаг: Given два описания {} и {} с синонимами слов'.format(d1, d2))
        context.d1 = d1
        context.d2 = d2

    @when(u'происходит предварительная обработка данных с синонимами')
    def step_impl(context):
        print(u'Шаг: When происходит предварительная обработка данных с синонинами')
        context.synonyms_d1 = preprocess_with_synonyms(context.d1)
        context.synonyms_d2 = preprocess_with_synonyms(context.d2)

    @then(u'результат сравнения {result} определяет, является ли одно описание менее точным, чем другое')
    def step_impl(context, result):
        ps = PS.SubSetPS()
        if (ps.is_less_precise(context.synonyms_d1, context.synonyms_d2)):
            result = 'd1 менее точно'
        elif (ps.is_less_precise(context.synonyms_d2, context.synonyms_d1)):
            result = 'd2 менее точно'
        else:
            result = 'd1 равно d2'
        print(u'STEP: Then результат сравнения {} определяет, является ли одно описание менее точным, чем другое'.format(result))

    @when(u'происходит предварительная обработка данных с антонимами')
    def step_impl(context):
        print(u'Шаг: When происходит предварительная обработка данных с антонимами')
        ps = AntonymPS()
        context.synonyms_d1, context.synonyms_d2 = ps.preprocess_data([context.d1, context.d2])



    @given(u'два описания {d1} и {d2} с антонимами слов')
    def step_impl(context, d1, d2):
        print(u'Шаг: Given два описания {} и {} с антонимами слов'.format(d1, d2))
        context.d1 = d1
        context.d2 = d2

    @given(u'заданы следующие шаблоны')
    def step_impl_given(context):
        print(u'Шаг: заданы следующие шаблоны:')
        context.patterns = []
        for row in context.table:
            pattern = set(row['Шаблоны'].strip('{}').split(','))
            pattern = {tuple(word.strip().strip("'") for word in item.split(',')) for item in pattern}
            context.patterns.append(pattern)

    @when(u'вызывается функция n_bin_attributes')
    def step_impl_when(context):
        context.ps = PS.NgramPS()
        context.actual_bin_attrs = context.ps.n_bin_attributes(context.patterns)

    @then(u'количество бинарных атрибутов равно количеству атрибутов, возвращенных функцией iter_bin_attributes')
    def step_impl_then(context):
        expected_bin_attrs = len(list(context.ps.iter_bin_attributes(context.patterns)))
        assert context.actual_bin_attrs == expected_bin_attrs, \
            f"Количество бинарных атрибутов {context.actual_bin_attrs}, " \
            f"ожидалось {expected_bin_attrs}."
