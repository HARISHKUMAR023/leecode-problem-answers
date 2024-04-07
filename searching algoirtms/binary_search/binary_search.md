``` python 
f = [1, 2, 3, 4, 5, 6, 7]
find = 5

low = 0
high = len(f) - 1

while low <= high:
    mid = (low + high) // 2  
    if f[mid] == find:
        print("Element found at index:", mid)
        break
    elif f[mid] < find:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found")
