### Full Pyramid Patterns

``` python
n=6
for i in range(n):
    for j in range(n-i):
        print(" " , end=" ")
   
    for k in range(0, 2*i+1):
        print("*", end=" ")
    print(" ")

``` 
### Output

``` shell
            *  
          * * *  
        * * * * *  
      * * * * * * *  
    * * * * * * * * *  
  * * * * * * * * * * *  