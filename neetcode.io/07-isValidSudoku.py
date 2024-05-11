class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        result = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if (i, board[i][j]) in result or (board[i][j], j) in result or (i//3, j//3, board[i][j]) in result:
                        return False
                    result.add((i, board[i][j]))
                    result.add((board[i][j], j))
                    result.add((i//3, j//3, board[i][j]))
        return True
            
                
    '''this is my first solution, passes 473/507 of the testcases.
        for i in range(len(board)):
            rowList = []
            for val in board[i]:
                if val.isdigit() == True:
                    rowList.append(val)
            if len(set(rowList)) != len(rowList):
                return False
        for i in range(len(board)):
            columnList = []
            for j in range(len(board)):
                if board[j][i].isdigit() == True:
                    columnList.append(board[j][i])
            if len(set(columnList)) != len(columnList):
                return False
        return True'''


    
    # if a digit, check if there is a duplicate in any of the columns
    # if a digit, check if there is a duplicate in any of the rows
    # must only contain digits 1-9.

    # to check column: go to board[i], then go to board[i][0] for every
    # i..

    # okay well we coudl brute force it or we could literally just make a list of the positions and then
    # compare duplicates using sets...
    # so if th eleemtn is not '.' we can createa  add to result set..
    # (row, element), (element, column), (square x, square y, element) -> this works bc element 2 can not be in row 1 twice
    # similarly it cannot be in column 1 twice.  when it comes to squares, we can sort them using a coordinate plane
    # so we can use integer division with the row and column to find the coordinates of teh square.
    # then if the element is insdie of the square twice, it is invalid.
    # so these sets guarantee uniqueness!

    # (THis problem makes me wanan cry I'm so bad at Suodku someone help eaaaaaaaaaaaaaa)