``` python 
class Solution:

    def restoreString(self, s: str, indices: List[int]) -> str:

         shuffled = [''] * len(s)

         for char, index in zip(s, indices):

                shuffled[index] = char

         return ''.join(shuffled)

     

        