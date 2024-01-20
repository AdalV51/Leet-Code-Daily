from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        left, right = [0] * n, [0] * n

        stack = []
        for i in range(n):
            # Find the Previous Less Element
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            left[i] = i - stack[-1] if stack else i + 1
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            # Find the Next Less Element
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            right[i] = stack[-1] - i if stack else n - i
            stack.append(i)

        # Calculate the sum of contributions
        return sum(a * l * r for a, l, r in zip(arr, left, right)) % MOD
