## <span style="color:green;">Given an array of integers</span>:<span style="color:red;"> [1, 2, 1, 3, 2]</span> and we are given some queries: [1, 3, 4, 2, 10]. For each query, we need to find out how many times the number appears in the array. For example, if the query is 1 our answer would be 2, and if the query is 4 the answer will be 0. 

``` python 
myarry = [1,2,1,3,2]

#careating empty hash map or hash table using python 
hash_map = {}

# storing the value of the myarry in hash table and and count the value 
for i in myarry:
    hash_map[i]= hash_map.get(i,0)+1

print("The value stored in hash map or hash table :",hash_map)
# get count and queries and printing in 
for number in hash_map:
    print ( f"the number {number} , count data is {hash_map.get(number,0)}")

```
### Output 
``` shell 
The value stored in hash map or hash table : {0: 2, 1: 1, 2: 1, 3: 1, 4: 2, 6: 1, 7: 1, 5: 1}
the number 0 , count data is 2
the number 1 , count data is 1
the number 2 , count data is 1
the number 3 , count data is 1
the number 4 , count data is 2
the number 6 , count data is 1
the number 7 , count data is 1
the number 5 , count data is 1
