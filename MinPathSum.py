# https://leetcode.com/problems/minimum-path-sum
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # take min of top or left
                if i == 0:
                    if j != 0:
                        grid[i][j] += grid[i][j-1]
                else: 
                    if j == 0:
                        grid[i][j] += grid[i-1][j]
                    else:
                        grid[i][j] += min(grid[i-1][j],grid[i][j-1])
        return grid[len(grid)-1][len(grid[i]) - 1]