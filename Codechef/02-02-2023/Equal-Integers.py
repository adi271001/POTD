Question Link: https://www.codechef.com/problems/INCREAR
    
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a<b:
        print(b-a)
    else:
        if (a-b)%2==0:
            print((a-b)//2)
        else:
            print((a-b)//2+2)
