Question Link: https://www.codechef.com/problems/TAXES
    
t = int(input())
while t:
    x=int(input())
    if x>100:
        print(x-10)
    else:
        print(x)
    t -= 1
