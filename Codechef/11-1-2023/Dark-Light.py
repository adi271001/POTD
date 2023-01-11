Question Link: https://www.codechef.com/problems/DARLIG
  
T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    if N % 4 == 0:
        if K == 0:
            print("OFF")
        else:
            print("ON")
    else:
        if K == 0:
            print("ON")
        else: 
            print("Ambiguous")
