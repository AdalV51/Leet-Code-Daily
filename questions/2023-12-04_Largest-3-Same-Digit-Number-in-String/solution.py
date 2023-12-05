class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest_good_integer = ""

        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                largest_good_integer = max(largest_good_integer, num[i : i + 3])

        return largest_good_integer
