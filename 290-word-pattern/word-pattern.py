class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        my={}
        p=s.split()
        c=0
        for i, j in zip(pattern,s.split()):
          if i not in my:
             if j not in my.values():
                my[i]=j
        
       
        for i in pattern:
            if len(pattern) != len(s.split()):
                # print(len(pattern),len(s.split()))
                return  False
            if i not in my:
                return False
            if my[i] != p[c]:
                 return False
            c+=1
        return True
        
        # my={}
            

        # for i, j in zip(pattern,s.split()):
        #     if i not in my:
        #      if j not in my.values():
        #         my[i]=j
        # c=0
        # # print(my)
        # p=s.split()
        # for i in pattern:
        #     # if i in my:
        #     #     return False
        #     #     break
        #     if my[i] != p[c]:
        #         # print(my[i] , p[c])
        #         return False
        #         break
        #     c+=1
        # print(True)