Question Link: https://my.newtonschool.co/playground/code/kn4lx2owrw9b

a,b=map(int,input().split())
c=0
for l in range(a+1,b):
    if(l%2==0 and c!=5):
        print(l,end=" ")
        c+=1
