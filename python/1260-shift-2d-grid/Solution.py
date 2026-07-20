class Solution(object):
    def shiftGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        total = m * n
        k = k % total
        
        flat_list = [val for row in grid for val in row]
        shifted_list = flat_list[-k:] + flat_list[:-k]
        
        return [shifted_list[i : i + n] for i in range(0, total, n)]