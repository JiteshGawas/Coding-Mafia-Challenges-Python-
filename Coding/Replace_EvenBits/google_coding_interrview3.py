n = int(input())
x= bin(n).replace('0b','')
print(x)
t=''
for i in range(len(x)):
    if(i%2==0):
        t=t + x[i].replace('1','0')
    else:
        t=t + x[i]
print(t)
