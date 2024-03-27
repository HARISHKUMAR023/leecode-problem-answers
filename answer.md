``` python
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row="qwertyuiop"
        second_row = "asdfghjkl"
        third_row="zxcvbnm"
        ans=[]
        for word in words:
            lower_word = word.lower()
            if all(char in first_row for char in lower_word):
                ans.append(word)
            elif all(char in second_row for char in lower_word):
                ans.append(word)
            elif all(char in third_row for char in lower_word):
                ans.append(word)

        return ans