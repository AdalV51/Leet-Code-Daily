import heapq
from collections import defaultdict
from typing import List


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_ratings = {}
        self.food_ratings_by_cuisine = defaultdict(list)
        self.highest_rated_food = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            # Negative rating because heapq is a min-heap and we want max-heap behavior
            heapq.heappush(self.food_ratings_by_cuisine[cuisine], (-rating, food))
            self.food_ratings[food] = (rating, cuisine)

        for cuisine in self.food_ratings_by_cuisine:
            self._update_highest_rated_food(cuisine)

    def _update_highest_rated_food(self, cuisine):
        while self.food_ratings_by_cuisine[cuisine]:
            rating, food = self.food_ratings_by_cuisine[cuisine][0]
            current_rating, _ = self.food_ratings[food]
            # Check if the top of the heap is still the highest rated food
            if -rating == current_rating:
                self.highest_rated_food[cuisine] = food
                return
            # Remove outdated entry
            heapq.heappop(self.food_ratings_by_cuisine[cuisine])

    def changeRating(self, food: str, newRating: int) -> None:
        rating, cuisine = self.food_ratings[food]
        # Update the rating
        self.food_ratings[food] = (newRating, cuisine)
        # Push new rating to the heap
        heapq.heappush(self.food_ratings_by_cuisine[cuisine], (-newRating, food))
        # Update the highest rated food for this cuisine
        self._update_highest_rated_food(cuisine)

    def highestRated(self, cuisine: str) -> str:
        self._update_highest_rated_food(cuisine)
        return self.highest_rated_food.get(cuisine, "Cuisine not found")


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
