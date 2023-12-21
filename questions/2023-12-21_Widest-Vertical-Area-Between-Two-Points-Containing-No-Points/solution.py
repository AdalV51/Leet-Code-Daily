from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points_width = sorted(list(set([point[0] for point in points])))
        biggest_difference = 0

        for index in range(1, len(points_width)):
            if (points_width[index] - points_width[index - 1]) > biggest_difference:
                biggest_difference = points_width[index] - points_width[index - 1]

        return biggest_difference
