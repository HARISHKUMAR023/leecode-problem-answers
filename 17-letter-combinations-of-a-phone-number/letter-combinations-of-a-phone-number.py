class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Mapping of digits to letters.
        digit_to_letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        # If the input is empty, return an empty list.
        if not digits:
            return []

        # This function will perform the backtracking.
        def backtrack(index, path):
            # If the current combination is complete, add it to the results.
            if index == len(digits):
                combinations.append("".join(path))
                return

            # Get the letters that the current digit maps to, and loop through them.
            current_digit = digits[index]
            for letter in digit_to_letters[current_digit]:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()  # backtrack

        combinations = []
        backtrack(0, [])
        return combinations
