class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       my=set()
       l=0
    
       maxi=0
       for r in range(len(s)):
         if s[r] in my:
            while  s[r] in my :
                my.remove(s[l])
                l+=1
         
         my.add(s[r])
         maxi=max(maxi , r-l+1)
          
       return maxi
         
        
        