class Solution:
    def reverseWords(self, s: str) -> str:
        word=[]
        w=""
        for i in s:
            
            if i == " ":
                if len(w) != 0:
                    word.append(w)
                    w=""
            else:
                w+=i
        if len(w) != 0:
            word.append(w)
        for  j in word:
            if j == "":
                word.remove(j)
        return " ".join(word[::-1])