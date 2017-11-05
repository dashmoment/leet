class node:
    def __init__(self, value):
        self.value = value
        self.up = None
        self.left = None

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        current_value = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
               
                if grid[i][j] == "1":
                    
                   
    
                    if i-1 >= 0 and grid[i-1][j] != "0":
                        grid[i][j] = grid[i-1][j]
                    elif j-1 >=0 and grid[i][j-1] != "0":
                        grid[i][j] = grid[i][j-1]
                    elif j+1 < len(grid[0]) and grid[i][j+1] != "0" and grid[i][j+1] != "1":
                        grid[i][j] = grid[i][j+1]
                    elif i+1 < len(grid) and grid[i+1][j] != "0" and grid[i+1][j] != "1":
                        grid[i][j] = grid[i+1][j]
                    
                    else:
                       
                        current_value = current_value-1
                        grid[i][j] = current_value
                    
                    if i+1 < len(grid) and grid[i+1][j] == "1":
                        grid[i+1][j] = grid[i][j]
                    if j+1 < len(grid[0]) and grid[i][j+1] == "1":          
                        grid[i][j+1] = grid[i][j]
        print(grid)
        return abs(current_value)

s = Solution()
print(s.numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))
