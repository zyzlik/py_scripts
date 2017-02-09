lab = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

[[1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,1],
[1,0,1,1,1,1,1,1,0,1,1,1],[1,0,1,0,0,0,0,0,0,0,0,1],[1,0,1,0,1,1,1,1,1,1,0,1],[1,0,1,0,1,0,0,0,0,0,0,1],[1,0,0,0,1,1,0,1,1,1,0,1],[1,0,1,0,0,0,0,1,0,1,1,1],[1,0,1,1,0,1,0,0,0,0,0,1],[1,0,1,0,0,1,1,1,1,1,0,1],[1,0,0,0,1,1,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1]]

start_point = [1, 1]
end_point = [len(lab) - 2, len(lab) - 2]


def mark_around(d, point):
    if point == 0:
        point = d + 1
    return point


def place_for_wave(lab):
    for row in lab:
        if 0 in row:
            return True
    return False


def find_path(lab, current, x, y):
    path = {
        (1, 0) : 'N',
        (-1, 0): 'S',
        (0, 1) : 'W',
        (0, -1): 'E' 
    }

    for i in range(-1, 2):
        for j in range(-1, 2):
            if lab[x+i][y+j] == current - 1:

                point = (x+i, y+j, path[(i, j)])
                return point




d = 2
lab[start_point[0]][start_point[1]] = d


while place_for_wave(lab) and lab[end_point[0]][end_point[1]] == 0:
    for i in range(0, len(lab)):
        for j in range(0, len(lab[i])):
            if lab[i][j] == d:
                lab[i+1][j] = mark_around(d, lab[i+1][j])
                lab[i-1][j] = mark_around(d, lab[i-1][j])
                lab[i][j+1] = mark_around(d, lab[i][j+1])
                lab[i][j-1] = mark_around(d, lab[i][j-1])
    d += 1

x = end_point[0]
y = end_point[1]
current = lab[x][y]
path = ''

while current != lab[start_point[0]][start_point[1]]:
    point = find_path(lab, current, x, y)
    x = point[0]
    y = point[1]
    path += point[2]
    current -= 1

print path
print path[::-1]