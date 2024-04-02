``` python
s = [9, 4, 2, 8, 10]

#  ====> Selection Sort <=====
for i in range(len(s)):
    min_index = i
    for j in range(i+1, len(s)):
        if s[j] < s[min_index]:
            min_index = j
    # Swap s[i] and s[min_index]
    t = s[i]
    s[i] = s[min_index]
    s[min_index] = t

print("After Selection Sort:", s)
