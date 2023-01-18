Question Link: http://www.codechef.com/problems/FINE
    
a=int(input())
for l in range(a):
    s=int(input())
    if(s<=70):
        print('0')
    elif(s>70 and s<=100):
        print('500')
    else:
        print('2000')
