class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
         b=s
         my=list(b)
         for i in my:
            if "".join(my) == goal:
                return True 
            my.append(my[0])
            my.remove(my[0])
            
         return False
        
            