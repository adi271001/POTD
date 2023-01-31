Question Link: https://www.codechef.com/problems/HELIUM3
    
k=int(input())
for l in range(k):
    b=list(map(int,input().split()))
    if b[0]*b[1]<=b[2]*b[3]:
        print("Yes")
    else:
        print("No")
