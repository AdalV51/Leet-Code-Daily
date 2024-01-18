class Solution:
    def climbStairs(self, n: int) -> int:
        prev_two_steps, prev_one_step, current_steps = 0, 1, 0

        for _ in range(n):
            current_steps = prev_two_steps + prev_one_step
            prev_two_steps, prev_one_step = prev_one_step, current_steps

        return prev_one_step
