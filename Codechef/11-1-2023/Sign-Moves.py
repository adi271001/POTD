Question Link: https://www.codechef.com/problems/SIGNMOVE
    
for _ in range(int(input())):

    n=int(input())

    ans=n//2
    if(n%2 != 0):
        print(-(ans+1))
    else:
        print(ans)
