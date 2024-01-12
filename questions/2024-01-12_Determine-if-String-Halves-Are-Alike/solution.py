class Solution:
    def __init__(self):
        self.vowels = {"a", "e", "i", "o", "u"}

    def number_of_vowels(self, s: str) -> int:
        return sum(char in self.vowels for char in s)

    def halvesAreAlike(self, s: str) -> bool:
        half_length = len(s) // 2
        first_half = s[:half_length].lower()
        second_half = s[half_length:].lower()

        return self.number_of_vowels(first_half) == self.number_of_vowels(second_half)
