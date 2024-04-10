Feature: Тестирование функции n_bin_attributes

      Scenario: Проверка функции n_bin_attributes
        Given заданы следующие шаблоны
        | Шаблоны |
        | {('hello', 'world')} |
        | {('hello', 'there')} |
        | {('hi',)} |
        | set() |
        When вызывается функция n_bin_attributes
        Then количество бинарных атрибутов равно количеству атрибутов, возвращенных функцией iter_bin_attributes