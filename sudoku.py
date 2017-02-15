matrix = [
[5,3,4,2,7,8,9,1,2],
[6,7,2,1,9,5,3,4,8],
[1,9,8,3,4,2,5,6,7],
[8,5,9,7,6,1,4,2,3],
[4,2,6,8,5,3,7,9,1],
[7,1,3,9,2,4,8,5,6],
[9,6,1,5,3,7,2,8,4],
[2,8,7,4,1,9,6,3,5],
[3,4,5,2,8,6,1,7,9]
];

def is_sudoku_valid(matrix):
     valid_row = [1,2,3,4,5,6,7,8,9]

     def check_row(row):
          if sorted(row) != valid_row:
               return False
          return True

     # check rows
     for row in matrix:
          if not check_row(row):
               print 'row'
               return False

     # check columns
     for row in zip(*matrix):
          if not check_row(row):
               print 'column'
               return False

     # check squares
     square = []
     for i in range(0, len(matrix), 3):
          for f in range(0, len(matrix), 3):
               for k in range(3):
                    for j in range(3):
                         square.append(matrix[k + i][j + f])
               if sorted(square) != valid_row:
                    return False
               square = []
     return True


print is_sudoku_valid(matrix)
