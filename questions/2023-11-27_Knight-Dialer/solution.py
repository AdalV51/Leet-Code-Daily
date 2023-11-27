from typing import Dict, List


class Solution:
    MOD = 10**9 + 7

    def knightDialer(self, n: int) -> int:
        """
        Calculate the number of distinct phone numbers of length n that can be dialed
        using a knight's move on a standard phone keypad.

        Args:
        n (int): The length of the phone number to dial.

        Returns:
        int: The number of distinct phone numbers modulo 10^9 + 7.
        """
        if n == 1:
            return 10  # Base case: Each digit is a valid phone number of length 1

        possible_movements = self.build_knight_movements()

        # Initialize dynamic programming table
        # dp[i][j] represents the number of distinct phone numbers of length i ending with digit j
        dp = [[0] * 10 for _ in range(n)]

        # Base case for dynamic programming
        for i in range(10):
            dp[0][i] = 1  # There is one way to dial a number of length 1 for each digit

        # Build the table using bottom-up approach
        for length in range(1, n):
            for digit in range(10):
                # For each possible next move from the current digit
                for next_digit in possible_movements[digit]:
                    # Add the count of combinations from the previous length
                    dp[length][next_digit] = (
                        dp[length][next_digit] + dp[length - 1][digit]
                    ) % self.MOD

        # The answer is the sum of all combinations of length n
        return sum(dp[n - 1]) % self.MOD

    def build_knight_movements(self) -> Dict[int, List[int]]:
        """
        Create a mapping of possible movements for each digit on the keypad
        based on a knight's move in chess.

        Returns:
        Dict[int, List[int]]: A dictionary where keys are digits and values are lists of reachable digits.
        """
        movements = [
            (-2, -1),
            (-2, 1),
            (-1, -2),
            (1, -2),
            (2, -1),
            (2, 1),
            (1, 2),
            (-1, 2),
        ]
        keypad = [(1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#")]
        possible_movements = {}

        for row in range(4):
            for col in range(3):
                if keypad[row][col] in {"*", "#"}:
                    continue
                moves = []
                for dx, dy in movements:
                    new_row, new_col = row + dx, col + dy
                    if (
                        0 <= new_row < 4
                        and 0 <= new_col < 3
                        and keypad[new_row][new_col] not in {"*", "#"}
                    ):
                        moves.append(keypad[new_row][new_col])
                possible_movements[keypad[row][col]] = moves

        return possible_movements
