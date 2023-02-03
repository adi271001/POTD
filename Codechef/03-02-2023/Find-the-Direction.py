Question Link: https://www.codechef.com/problems/FACEDIR
    
k = int(input())
for l in range(k):
    a=int(input())
    if a%4==0:
        print('North')
    elif a%4==1:
        print('East')
    elif a%4==2:
        print('South')
    elif a%4==3:
        print('West')
    else:
        continue
