class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        previous_result = None
        for row in obstacleGrid:
            result_row = []
            for ind, grid in enumerate(row):
                if grid:
                    result_row.append(0)
                    continue
                if ind == 0 and not previous_result:
                    result_row.append(1)
                    continue                    
                result_grid = 0
                if ind != 0:
                    result_grid += result_row[-1]
                if previous_result:
                    result_grid += previous_result[ind]
                result_row.append(result_grid)
            previous_result = result_row
        return result_row[-1]


grid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
sol = Solution()
print sol.uniquePathsWithObstacles(grid)

