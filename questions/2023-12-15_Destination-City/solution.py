from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        origin_cities = set()
        destination_cities = set()

        for origin_city, destination_city in paths:
            origin_cities.add(origin_city)
            destination_cities.add(destination_city)

        return list(destination_cities - origin_cities)[0]
