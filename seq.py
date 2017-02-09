seq = [
    [1, 2, 1, 1],
    [1, 1, 4, 1],
    [1, 3, 1, 6],
    [1, 7, 2, 5]
]


def find_seq_row(matrix):
    for row in seq:
        uniq = set(row)
        for digit in uniq:
            if row.count(digit) == 4:
                return digit

seq = zip(*seq)
print seq

find_seq_row(seq)
