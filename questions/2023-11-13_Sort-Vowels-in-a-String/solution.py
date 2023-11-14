class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"

        # Extract and sort the vowels from the string
        sorted_vowels = sorted([char for char in s if char in vowels])

        # Iterate through the string and replace vowels with sorted vowels
        sorted_vowels_iter = iter(sorted_vowels)
        result = [next(sorted_vowels_iter) if char in vowels else char for char in s]

        return "".join(result)
