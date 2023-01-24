Question Link: https://www.codechef.com/problems/PASSTHEEXAM
    
p=int(input())
for k in range(p):
    r,s,t=map(int,input().split())
    if (r+s+t)>=100:
        if r>=10 and s>=10 and t>=10:
            print("PASS")
        else:
            print("FAIL")
    else:
        print("FAIL")
