class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        square = 0
        common_lines = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    square += 1
                    if i > 0 and grid[i-1][j] == 1:
                        common_lines += 1
                    if j > 0 and grid[i][j-1] == 1:
                        common_lines += 1
        return square * 4 - common_lines * 2