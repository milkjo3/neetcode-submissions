class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()

        def dfs(i, j):
            directions = [[0,1], [1,0], [-1,0], [0, -1]]
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            if (i,j) in visit:
                return 0 
            visit.add((i,j))
            perim = 0 
            for direction in directions:
                perim += dfs(i + direction[0], j + direction[1])

            return perim

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i,j)


