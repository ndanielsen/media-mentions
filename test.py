def findPath(matrix):
    
    def ordered(row):
        row_foward = sorted(row)
        row_backwards = sorted(row, reverse=True) 
        if row_foward == row:
            return True
        elif row_backwards == row:
            return True
        else:
            return False
    
    for r in matrix:
        if not ordered(r):
            return False
    return True

matrix = [[1,2,3], 
 [6,5,4], 
 [7,8,9], 
 [12,11,10]]

matrix2 = [[2,3,4,5], 
 [1,8,7,6], 
 [12,9,10,11]]

matrix3 = [[2,3], 
 [1,4], 
 [10,5], 
 [7,6], 
 [8,9]]


if __name__ == '__main__':
    print findPath(matrix3)