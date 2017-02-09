"""
This    is  a   simple  doctest that    checks  some    of  Python's    arithmetic
operations.
>>> 2   +   2
4
>>> 3   *   3
10
"""



def count_neighbours(grid, row, col):
    count = 0
    for i in range(len(grid)):
        if i >= row-1 and i <= row+1:
            for k in range(len(grid[i])):
                if k >= col-1 and k <= col+1:
                    if grid[i][k] == 1:
                        count += 1
    if grid[row][col] == 1:
        count -= 1
        
    print count
    


def multiple(a, b):
    return a*b

assert(multiple(2,2) == 4)
if __name__ == '__main__':
    import timeit
    print(timeit.timeit("count_neighbours([[1,1,1],[0,0,0],[0,1,1]], 0, 1)", setup="from __main__ import count_neighbours"))