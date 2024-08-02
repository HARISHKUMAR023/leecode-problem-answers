class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       my = {}
       maxi = 0
       start = 0
       for i in range(len(s)):
          if s[i] in my and my[s[i]] >= start:
             start = my[s[i]]+1
          my[s[i]]=i
          maxi = max(maxi , i - start +1)
       return maxi
        
        