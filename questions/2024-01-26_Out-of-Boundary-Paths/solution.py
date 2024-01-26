class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        ROWS, COLS = m, n
        MOD = 10**9 + 7
        cache = {}

        def dfs(row, column, moves):
            if row < 0 or row == ROWS or column < 0 or column == COLS:
                return 1
            if moves == 0:
                return 0
            if (row, column, moves) in cache:
                return cache[(row, column, moves)]

            cache[(row, column, moves)] = (
                dfs(row + 1, column, moves - 1)
                + dfs(row - 1, column, moves - 1)
                + dfs(row, column + 1, moves - 1)
                + dfs(row, column - 1, moves - 1)
            )

            return cache[(row, column, moves)] % MOD

        return dfs(startRow, startColumn, maxMove)
