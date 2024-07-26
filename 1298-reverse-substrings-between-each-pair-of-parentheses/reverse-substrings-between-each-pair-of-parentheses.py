
class Solution:
    def reverseParentheses(self, s: str) -> str:
        sa=[]
        for i in s:
            if i == ')':
                sub=[]
                while sa and sa[-1] != '(':
                    sub.append(sa.pop())
                sa.pop()
                sa.extend(sub)
            else:
                sa.append(i)
        return ''.join(sa)
        