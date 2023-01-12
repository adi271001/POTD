Question Link: https://www.codechef.com/problems/FRUITS
    
for x in range(int(input())):
    A,O,K=map(int,input().split())
    if A==O:
        print(0)
        continue
    s=min(A,O)
    b=max(A,O)
    print(0) if s+K>=b else print(b-(s+K))
