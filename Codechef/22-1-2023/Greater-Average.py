Question Link: https://www.codechef.com/problems/AVGPROBLEM
    
for t in range(int(input())):
    x,y,z = map(int,input().split())
    if(((x+y)/2)>z):
        print("yes")
    else:
        print('no')
