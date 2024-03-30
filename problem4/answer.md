``` python 
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
           c =0
          
           for i in items:
            
                if ruleKey =="color":

                    c1=1
                    if ruleValue == i[c1]:
                        c+=1
                if ruleKey == "name":
                    N1=2
                   
                    if ruleValue == i[N1]:
                        c+=1
                if ruleKey == "type":
                    t1=0
                    if ruleValue == i[t1]:
                        c+=1
                    
           return c