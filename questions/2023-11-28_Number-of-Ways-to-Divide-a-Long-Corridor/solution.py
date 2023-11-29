class Solution:
    def numberOfWays(self, corridor: str) -> int:
        total_seats = 0
        current_pair = []  # Tracks the indices of the current pair of seats
        possible_splits = 1  # Accumulates the number of ways to split

        for index, spot in enumerate(corridor):
            if spot == "S":
                total_seats += 1

                # When a pair is completed, calculate the possible splits
                if len(current_pair) == 2:
                    possible_splits *= index - current_pair[-1]
                    current_pair = []
                current_pair.append(index)

        # If there are no seats or an odd number of seats, return 0
        if total_seats == 0 or total_seats % 2 == 1:
            return 0

        return possible_splits % (10**9 + 7)
