class Solution:
    def myAtoi(self, s: str) -> int:
        # v=s.lstrip()
        # ans=""
        # for i in v:
        #     if 'a' <= v[0] <= 'z' or 'A' <= v[0] <= 'Z':
        #         return 0
        #         break
        #     if v[0] != "-":
        #         if i == '+' or i == '-' or i ==  '.' or i == '_' or 'a' <= i <= 'z' or 'A' <= i <= 'Z':
        #             # print(0)
        #             # ans=0
        #             break
        #         else:
        #             ans+=i
        #     else:
        #         ans+=i
        # return int(ans)
        s = s.lstrip()  # Step 1: Remove leading whitespace
        if not s:
            return 0

        sign = 1  # Default sign is positive
        result = 0
        index = 0

        # Step 2: Check for optional sign
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1

        # Step 3: Convert digits to integer
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1

        # Apply sign to result
        result *= sign

        # Step 4: Clamp result within 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result
                