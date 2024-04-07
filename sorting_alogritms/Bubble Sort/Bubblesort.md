``` python 
# Bubble Sort

s = [9, 4, 2, 8, 10]

for i in range(len(s)):
    for j in range(i+1, len(s)):
        if s[i] > s[j]:
            # Swap s[i] and s[j]
            t = s[i]
            s[i] = s[j]
            s[j] = t

print("After Bubble Sort:", s)