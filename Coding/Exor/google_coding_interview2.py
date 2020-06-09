from array import *
n=int(input())
arr = array('i',[])
for i in range(n):
    x= int(input())
    arr.append(x)
count = 0
for i in range(n-1):
    j=0
    if(arr[i]^arr[j]==0):
        j+=1
        count = count+1
    
print("No of pairs having XOR as 0 are",+count)