from itertools import combinations

t1 = ({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})
t2 = ({3,4},{5,6},{2,7},{1,5},{2,6},{8,4},{1,7},{4,5},{9,5},{2,3},{8,2},{2,4},{9,6},{5,7},{3,6},{1,3},)
t3 = ({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})


def ring_amount(rings):
    amount = 0
    for pair in rings:
        for ring in pair:
            if ring > amount:
                amount = ring
    return amount


def destroy(ring, rings):
    lst = []
    for pair in rings:
        if ring in pair:
            pass
        else:
            lst.append(pair)
    return lst


ring_amount = ring_amount(t3)
max_count = ring_amount - 1
for i in range(1, ring_amount):
    for order in combinations(range(1, ring_amount + 1), i):
        rings_copy = list(t3)
        for ring in order:
            rings_copy = destroy(ring, rings_copy)
        if not rings_copy:
            print str(len(order))