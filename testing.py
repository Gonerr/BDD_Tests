# from paspailleur import pattern_structures as PS
# d1= (1.5, 3.14)
# d2 = (2, 3)
# ps = PS.IntervalPS()
# assert ps.is_less_precise(d1, d2)

from paspailleur import pattern_structures as PS

# Описания данных
d1 = {('hello', 'world'), ('!',)}
d2 = {('hello', 'world', '!')}

# Создание объекта NgramPS
ps = PS.NgramPS()

# Проверка, является ли d1 менее точным, чем d2
print (ps.is_less_precise(d1, d2))
