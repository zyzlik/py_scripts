# -*- coding: utf-8 -*-

"""
Given coords of rectangles, we should count the area of the shape it makes
"""


coords = [
    [0, 1, 3, 3],
    [2, 2, 6, 4],
    [1, 0, 3, 5],
    [7, 2, 8, 3],
    [10, 6, 11, 8]
]

# Ищем саму левую координату x
# Looking for the leftmost coord of x


def find_left(coords):
    left_x = coords[0][0]
    for coord in coords:
        if left_x >= coord[0]:
            left_x = coord[0]
    return left_x

# Ищем самую правую координату x
# Looking for the rightmost coord of x


def find_right(coords):
    right_x = coords[0][2]
    for coord in coords:
        if right_x < coord[2]:
            right_x = coord[2]
    return right_x

# Сканируем, какая площадь занята между указанной координатой и следующей
# Scan the area between x_coord and next coord


def scan_y(x_coord):
    y_coord = []
    area = 0
    for coord in coords:
        if x_coord >= coord[0] and x_coord < coord[2]:
            y_coord.append(range(coord[1], coord[3] + 1))
    if len(y_coord) == 1:
        area += y_coord[0][-1] - y_coord[0][0]
    elif len(y_coord) > 1:
        tmp = []
        for lst in y_coord:
            for coord in lst:
                if coord not in tmp:
                    tmp.append(coord)
                    tmp.sort()
        for i in range(len(tmp) - 1):
            if (tmp[i + 1] - tmp[i]) == 1:
                area += 1
            else:
                continue
    return area


def main(coords):
    area = 0
    for X in range(find_left(coords), find_right(coords) + 1):
        area += scan_y(X)
    return area


print main(coords)
