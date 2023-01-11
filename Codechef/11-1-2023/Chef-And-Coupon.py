Question Link: https://www.codechef.com/problems/COUPON2
    
for i in range(int(input())):
    d,c =  map(int,input().split())
    a1,a2,a3 = map(int,input().split())
    b1,b2,b3 = map(int,input().split())
    
    A = a1+a2+a3
    B = b1+b2+b3
    
    if A>=150 and B>=150 :
        if A+B+c < A+B+d+d:
            print("Yes")
        else:
            print("No")
    
    elif A>=150 or B>=150:
        if A+B+d+c < A+B+d+d:
            print("Yes")
        else:
            print("No")
    
    else:
        print("No")
