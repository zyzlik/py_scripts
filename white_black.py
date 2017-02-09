def count_prob(seq, n):
    lst = list(seq)
    length = float(len(lst))

    def take_black(lst):
        new_lst = lst[:]
        new_lst.remove('b')
        new_lst.append('w')
        return new_lst

    def take_white(lst):
        new_lst = lst[:]
        new_lst.remove('w')
        new_lst.append('b')
        return new_lst

    if n > 1:
        print n
        print 'variants are: '
        print take_black(lst)
        print 'and'
        print take_white(lst)
        n -= 1
        if 'b' in lst:
            new = take_black(lst)
            count_prob(new, n)
        if 'w' in lst:
            new = take_white(lst)
            count_prob(new, n)


for i in PosibleCombinations:
    if i not in result:
        result[i] = {}
    for j in PosibleCombinations:
        if j not in result:
            result[j] = {}
        if i == j:
            continue
        else:
            if sum([1 for k0, k1 in enumerate(i) if j[k0] != k1]) == 1:
                if sum(i) > sum(j):
                    result[i][j] = Fraction(sum(i), pearls)
                else:
                    result[i][j] = 1 - Fraction(sum(i), pearls)


print count_prob('wbb', 3)
