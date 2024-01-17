import random
from typing import Dict, List


class RandomizedSet:
    def __init__(self) -> None:
        self.elements: List[int] = []
        self.indices: Dict[int, int] = {}

    def contains(self, value: int) -> bool:
        return value in self.indices

    def insert(self, value: int) -> bool:
        if self.contains(value):
            return False

        self.elements.append(value)
        self.indices[value] = len(self.elements) - 1
        return True

    def remove(self, value: int) -> bool:
        if not self.contains(value):
            return False

        index_to_remove: int = self.indices[value]
        last_element: int = self.elements[-1]
        self.elements[index_to_remove] = last_element
        self.indices[last_element] = index_to_remove

        self.elements.pop()
        del self.indices[value]
        return True

    def getRandom(self) -> int:
        return random.choice(self.elements)
