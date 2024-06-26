class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source=set()
        for i in paths:
          source.add(i[0])
        for j in paths:
          if j[1] not in source:
             return j[1]