from collections import Counter
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # Create a set of unique winners and a counter for losers
        unique_winners = set(match[0] for match in matches)
        loss_count = Counter(match[1] for match in matches)

        # Find players who won every match (no record of losing)
        undefeated_players = [
            player for player in unique_winners if player not in loss_count
        ]

        # Find players who lost exactly one match
        players_lost_once = [
            player for player, losses in loss_count.items() if losses == 1
        ]

        # Return the sorted lists of undefeated players and players who lost exactly once
        return [sorted(undefeated_players), sorted(players_lost_once)]
