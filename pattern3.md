```
for i in range(1, 4):
    for j in range(i, 6):
        print(j, end="")
    for j in range(1, i):
        print(j, end="")
    print()
```
### output
```
12345
23451
34512
```
