### insertionsort algoritms in python

``` python 

# [ 3,4,6,2,7]
# for loop start form 1 to n :
for  i in range(1,len(n)):
    #key=4
    key = n [i]
    #j = 0 
    j = i - 1

    while j >= 0 and key < n[j]:
        n[j+1] = n[j]
        j=j-1
    #n[1]=4
    n[j+1] = key
print(n)