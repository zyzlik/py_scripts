# -*- coding: utf-8 -*-
'''
It is very old script. I really don't remember what it does :)
Храним результаты в списке, сортируем их, каждый новый вариант проверяем на вхождение.
Результат - длина получившего списка.
Создаем такое количество циклов for, сколько k
То есть, если k > 0, то создаем цикл
'''


n = 10
k = 4
max_val = n - k + 1

var = []

for i in range(0, k):
    var.append(1)

result = []


def cycle(n, k):
    global var, max_val, result
    if k > 0:
        for i in range(1, max_val + 1):
            var[k - 1] = i
            sum = 0
            for x in var:
                sum += x
            if sum == n:
                tmp = list(var)
                tmp.sort()
                if tmp not in result:
                    result.append(tmp)
            cycle(n, k - 1)


cycle(n, k)
print result
print len(result)
