str = input("Enter the string")
def sort_seperately(str):
    up =[]
    low = []
    for i in str:
        if(i.isupper()):
            up.append(i)
        else:
            low.append(i)
    up=sorted(up)
    low=sorted(low)
    ans = []
    k=0
    j=0
    for i in range(len(str)):
        if(str[i].isupper()):
            ans.append(up[k])
            k=k+1
        else:
            ans.append(low[j])
            j=j+1
    res=''
    for ele in ans:
        res=res+ele
    print(res)
    
sort_seperately(str)