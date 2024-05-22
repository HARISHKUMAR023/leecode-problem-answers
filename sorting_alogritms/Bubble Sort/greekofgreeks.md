### Link for problem in greek of greeks
 [code] (https://www.geeksforgeeks.org/problems/bubble-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=bubble-sort)

 ### Answer in python 

 ``` python 


class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        # code here
       for i in range(len(arr)):
           for j in range(i+1,len(arr)):
               if arr[i] > arr[j]:
                   t=arr[i]
                   arr[i]=arr[j]
                   arr[j]=t
                   