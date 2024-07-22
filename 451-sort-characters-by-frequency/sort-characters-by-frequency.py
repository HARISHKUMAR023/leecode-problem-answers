class Solution:
    def frequencySort(self, s: str) -> str:
        my = {}
        for i in s:
            my[i] = my.get(i, 0) + 1

        # Step 2: Create a list of (character, frequency) tuples and sort by frequency
        sorted_items = sorted(my.items(), key=lambda item: item[1], reverse=True)
        
        # Step 3: Build the result string based on sorted frequencies
        ans = ""
        for char, freq in sorted_items:
            ans += char * freq
        
        return ans