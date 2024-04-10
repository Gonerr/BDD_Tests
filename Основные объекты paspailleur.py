from paspailleur import pattern_structures as PS

# # Описания для сравнения
# d1 = (1.5, 3.14)
# d2 = (2, 3)
#
# # Создание объекта IntervalPS
# ps = PS.IntervalPS()
#
# # Проверка, является ли d1 менее точным, чем d2
# assert ps.is_less_precise(d1, d2)
# print(ps.is_less_precise(d1, d2))
#
# # Задание двух описаний d1 и d2
# d1 = {'банан', 'апельсин', 'яблоко'}
# d2 = {'банан', 'апельсин', 'яблоко', 'лимон'}
#
# ps = PS.SubSetPS()
#
# # Проверка, является ли описание d2 менее точным, чем описание d1 в контексте Pattern Structure SubSetPS
# print(ps.is_less_precise(d2, d1))
#
#
# # Описания данных
# d1 = [(1.5, 3.14), {'зеленые кубики'}, {'зеленые', 'желтые', 'красные'}]
# d2 = [(2, 3), {'зеленые кубики', 'тяжелые'}, {'зеленые', 'желтые'}]
# basic_structures = [PS.IntervalPS(), PS.SubSetPS(), PS.SuperSetPS()]
#
# # Создание объекта CartesianPS
# ps = PS.CartesianPS(basic_structures)
#
# # Проверка, является ли d1 менее точным, чем d2
# print(ps.is_less_precise(d1, d2))
#
#
# # Описания данных
# d1 = {('hello', 'world'), ('!',)}
# d2 = {('hello', 'world', '!')}
#
# # Создание объекта NgramPS
# ps = PS.NgramPS()
#
# # Проверка, является ли d1 менее точным, чем d2
# print( ps.is_less_precise(d1, d2) )


# Описания данных
d1, d2 = 'world', 'children'
ps = PS.SynonymPS()
pattern1, pattern2 = ps.preprocess_data([d1, d2])
# assert ps.is_less_precise(pattern1, pattern2)

print('pattern1:', pattern1)
print('pattern2:', pattern2)

# # Описания данных
# d1, d2 = 'good', 'good day'
# # Создание объекта AntonymPS
# ps = PS.AntonymPS()
# # Предварительная обработка данных
# pattern1, pattern2 = ps.preprocess_data([d1, d2])
# # Проверка, является ли pattern1 менее точным, чем pattern2
# assert ps.is_less_precise(pattern1, pattern2)
# # Вывод результатов
# print('pattern1:', pattern1)
# print('pattern2:', pattern2)