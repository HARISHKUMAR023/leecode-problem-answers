### Character Hashing:
#### Given the string: “abcdabefc” we are given some queries: [a, c, z]. For each query, we need to find out how many times the character appears in the string. For example, if the query is ‘a’ our answer would be 2, and if the query is ‘z’ the answer will be 0. 

``` python 
s=['a', 'b', 'c','d','r','a']

my_hash={}
for i in s:
    if i in my_hash:
        my_hash[i]+=1
    else:
        my_hash[i]=1

print(my_hash)

q=['a','b','c','d' ]
    
for j in q:
    print(f"The char count is {j} , {my_hash.get(j,0)}")
    

``` 
### output 
``` shell
{'a': 2, 'b': 1, 'c': 1, 'd': 1, 'r': 1}
The char count is a , 2
The char count is b , 1
The char count is c , 1
The char count is d , 1
