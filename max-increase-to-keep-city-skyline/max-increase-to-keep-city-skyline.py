class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        topbot = []
        leftright = []
        for c in range(len(grid[0])):
            max = 0
            for r in range(len(grid)):
                if grid[r][c] > max:
                    max = grid[r][c]
            topbot.append(max)
        
        for r in range(len(grid)):
            max = 0
            for c in range(len(grid[0])):
                if grid[r][c] > max:
                    max = grid[r][c]
            leftright.append(max)
        
        sum = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                arr = [topbot[c], leftright[r]]
                sum += min(arr) - grid[r][c]
        return sum
            
        