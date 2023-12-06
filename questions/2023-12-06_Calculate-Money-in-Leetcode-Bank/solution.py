class Solution:
    def totalMoney(self, n: int) -> int:
        """
        Calculate the total money saved over n days with a specific savings pattern.
        Each week starts with a certain amount saved on Monday, increasing by 1 each day.
        Each subsequent Monday starts with 1 more than the previous Monday.
        """
        total_money = 0
        weeks = n // 7
        remaining_days = n % 7

        for week in range(weeks):
            start_of_week_money = week + 1
            total_money += sum(range(start_of_week_money, start_of_week_money + 7))

        if remaining_days > 0:
            start_of_week_money = weeks + 1
            total_money += sum(
                range(start_of_week_money, start_of_week_money + remaining_days)
            )

        return total_money
