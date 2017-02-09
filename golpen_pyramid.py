t = (
    (1,),
    (2, 3),
    (3, 3, 1),
    (3, 1, 5, 4),
    (3, 1, 3, 1, 3),
    (2, 2, 2, 2, 2, 2),
    (5, 6, 4, 5, 6, 4, 3)
)

t1 = (
    (1,),
    (2, 3),
    (4, 6, 3)
)

t2 = (
    (1,),
    (3, 4),
    (6, 9, 6)
)


def count_gold(pyramid):
    pyramid_copy = list(list(row) for row in pyramid)
    for i in range(len(pyramid_copy) - 2, -1, -1):
        row = pyramid_copy[i]
        for j in range(len(row)):
            pyramid_copy[i][j] += max(pyramid_copy[i+1][j], pyramid_copy[i+1][j+1])
    return pyramid_copy[0][0]


print(count_gold(t))
