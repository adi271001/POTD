Question Link: https://www.codechef.com/problems/PROBCAT
    
k=int(input())
for l in range(k):
    p=int(input())
    if(p>=1 and p<100):
        print("Easy")
    elif(p>=100 and p<200):
        print("Medium")
    else:
        print("Hard")
