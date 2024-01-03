from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        laser_beams_per_row = [row.count("1") for row in bank if "1" in row]

        if len(laser_beams_per_row) < 2:
            return 0

        return sum(a * b for a, b in zip(laser_beams_per_row, laser_beams_per_row[1:]))
