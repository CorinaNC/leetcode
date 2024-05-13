class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ret = [[0] * (len(grid)-2) for i in range(len(grid)-2)]
        for i in range(len(grid)-2): # row
            for j in range(len(grid)-2): # col
                for row in range(i, i+3):
                    for column in range(j, j+3):
                        ret[i][j] = max(ret[i][j], grid[row][column])
        return ret
# okay so, we have [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
# maxLocal must be created which is size (n-2)* x (n-2)... so.. to creat that from this
# matrix.. for i in range(len(grid)), we know i is equal to the rows, in anested loop j is equal to the columns
# so we couild go from range(len(grid-2)) for the output..
# then iterate through the 3x3 square input anc compare the maximum
