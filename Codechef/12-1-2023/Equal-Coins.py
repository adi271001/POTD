Question Link: https://www.codechef.com/problems/EQUALCOIN
    
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if((x+2*(y))%2!=0):
        print("no")
        
    else:
        if( x==0 and y%2!=0):
            print("no")
        
        else:
            print("yes")
