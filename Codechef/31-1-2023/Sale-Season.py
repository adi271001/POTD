Question Link: https://www.codechef.com/problems/SALESEASON
    
k=int(input())
for l in range(k):
    b=int(input())
    if(b<=100):
        print(b)
    elif(b>100 and b<=1000):
        print(b-25)
    elif(b>1000 and b<=5000):
        print(b-100)
    elif(b>5000):
        print(b-500)
    else:
        print(" ")
