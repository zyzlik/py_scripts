# -*- coding: utf-8 -*-

# 1. Напишите класс, который хранит список своих экземпляров
# и позволяет итерировать по ним.


class Keeper:
    list_instances = []

    def __init__(self):
        Keeper.list_instances.append(self)

    def __del__(self):
        Keeper.list_instances.remove(self)

a = Keeper()
b = Keeper()

for i in Keeper.list_instances:
    print i

# Выведет
# <__main__.Keeper instance at 0x7f9076b8f950>
# <__main__.Keeper instance at 0x7f9076b8f908>


# 2. В чем отличие (i for i in arr) от [i for i in arr]?

# ########################### ОТВЕТ: ##############################
# Первое – создается объект-генератор, по которому можно проходить,
# используя метод next().
# Второе – генераторное выражение, просто создает список.
# #################################################################

# Напишите генератор следующего вида
# gen = reverse_gen([1, 2, 3, 4])
# >>> gen.next()
# 4
# >>> gen.next()
# 3
# >>> gen.next()
# 2
# >>> gen.next()
# 1
# >>> gen.next(
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# StopIteration

def reverse_gen(iterable):
    iterable.reverse()
    return (x for x in iterable)

gen = reverse_gen([1, 2, 3, 4])
print gen.next()
print gen.next()

# 3. Есть следующая функция:
#     def myappend(a = [], num = 0):
#          a.append(num)
#         print a
# Что будет происходить при выполнении следующего кода и почему:
#     >>> a = [1,2,3]
#     >>> myappend(a)
#     >>> myappend()
#     >>> myappend()

# ########################### ОТВЕТ: ##############################
# В первом случае (>>> a = [1,2,3], >>> myappend(a)) к списку a добавится значение
# num, то есть 0, результат будет [1,2,3,0]. Далее - вызов функции без аргументов, 
# соответственно, используется дефолтное значение, определенное в функции, то есть [].
# Результат = [0]. После следующего вызова = [0, 0].
# Так присходит потому, что изменяемые объекты, такие как списки и словари,
# передаются в виде ссылок на область памяти, где находится объект. Соответсвенно,
# Переменная a в локальной области видимости функции всегда ссылается на одно и тоже
# место. Проверить можно, например, указав в функции что-то вроде print a.__init__,
# выведется запись такого рода: <method-wrapper '__init__' of list object at 0x7fbdcd565638>
# адрес объекта при каждом выове будет один и тот же.
# #################################################################

# 4. Что такое декораторы? Для чего они нужны?

# ########################### ОТВЕТ: ##############################
# Декратор - фунция, который принимает в виде аргументы другую функцию,
# Производит определенные действия до нее/после нее/с результатом выполнения
# этой функции.
# Нужны в том случае, если необходимо, например, расширить функцию,
# не переписывая ее
# #################################################################

# Напишите кеширующий декоратор, который можно применить к функции
# get_long_response и который, если результат уже есть в кеше CACHE,
# вернет его, а если нет, то закеширует результат выполнения функции
# в CACHE и вернет его (результат).
# Результат выполнения функции get_long_response
# уникален для ее параметра user_id.


class Cache(object):
    __cache = {}
    __slots__ = '__cache'

    @classmethod
    def get(cls, key):
        print 'get', key
        return cls.__cache[key]

    @classmethod
    def set(cls, key, value):
        print 'set', key, value
        cls.__cache[key] = value

    @classmethod
    def has(cls, key):
        print 'has', key
        return key in cls.__cache

CACHE = Cache()


def cache_decorator(func):
    def wrapper(arg):
        c = Cache()
        if c.has(arg):
            return c.get(arg)
        else:
            result = func(arg)
            c.set(arg, result)
            return result
    return wrapper


@cache_decorator
def get_long_response(user_id):
    return user_id * 1000


print get_long_response(12)
print
print get_long_response(15)
print
print get_long_response(12)
print

# Напишите код приложения для Django 1.7, в котором у пользователей
# есть помимо основных полей 2 дополнительных: ИНН (может повторяться
# у разных пользователей, пользователей в системе может быть очень много)
# и счет (в рублях, с точностью до копеек). Также есть форма состоящая
# из полей:
# Выпадающий список со всем пользователями в системе,
# со счета которого нужно перевести деньги
# Текстовое поле для ввода ИНН пользователей,
# на счеты которых будут переведены деньги
# Текстовое поле для указания какую сумму нужно перевести с одного счета на другие
# Необходимо проверять есть ли достаточная сумма у пользователя,
# со счета которого списываются средства, и есть ли пользователи
# с указанным ИНН в БД. При валидности формы необходимо указанную
# сумму списать со счета указанного пользователя и перевести
# на счета пользователей с указанным ИНН в равных частях
# (если переводится 60 рублей 10ти пользователям, то каждому
# попадет 6 рублей на счет). Было бы неплохо, если бы
# форма работала без перезагрузки страницы.

# ########################### ОТВЕТ: ##############################
# https://github.com/zyzlik/account-project
# #################################################################

# 6. (Опционально) На входе - артикул (формат:
# последовательности цифр и букв разделены точкой или пробелом).
# необходимо заменить точки на пробелы и пробелы на точки
# с учетом всех возможных комбинаций.
# Например, на входе артикул (разделители только точки)
# 1.2.3
# На выходе должно быть:
# 1.2.3
# 1 2.3
# 1.2 3
# 1 2 3


from itertools import product, chain


def flatten(listOfLists):
    return chain.from_iterable(listOfLists)


def articul_comb(articul):
    # Собираем все не точки и не пробелы в отдельный список
    l = articul.split()

    for i in range(len(l)):
        if not l[i].isalnum():
            new_list = l[i].split('.')
            for k in new_list:
                l.insert(i + 1, k)
            l.pop(i)

    # Количество точек или пробелов на один меньше длины списка l
    combs = product('. ', repeat=len(l) - 1)
    for c in combs:
        combination = zip(l, c)
        # длины списков не равны, добавляем последний элемент
        combination.append(l[-1])
        if ''.join(flatten(combination)) != articul:
            print ''.join(flatten(combination))

articul_comb('qq.www.e 11')
