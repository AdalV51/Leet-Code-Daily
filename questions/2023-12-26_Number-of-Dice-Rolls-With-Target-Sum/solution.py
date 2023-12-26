class Solution:
    def numRollsToTarget(self, n, k, target):
        MOD = 10**9 + 7  # The modulo value given in the problem

        # Initialize the dp array with all zeros, extra space is used for ease of index management
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        # Base case: There is 1 way to roll 0 dice to get sum 0
        dp[0][0] = 1

        # Fill the dp array
        for dice in range(1, n + 1):
            for t in range(1, target + 1):
                for face in range(1, min(k, t) + 1):
                    # Update the number of ways to get to the current sum 't' using 'dice'
                    dp[dice][t] += dp[dice - 1][t - face]
                    dp[dice][t] %= MOD  # Take modulo to prevent integer overflow

        # The answer is the number of ways to roll 'n' dice to get 'target' sum
        return dp[n][target]
