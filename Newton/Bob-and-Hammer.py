Question Link: https://my.newtonschool.co/question-of-the-day?leaderboardType=fastest_today
    
 a, b, c = map(int, input().split())
if(a*b>=0 and a>=0):
    if b>a:
        print(a)
    elif c>b and a>b:
        print(-1)
    elif c>b:
        print(a)
elif(a*b>=0 and a<=0 and b<=0):
    if(a>b or (a<b and c<=0 and b<c)):
        print(abs(a))
    elif a<b and b<c:
        print(2*c-a)
    elif b>a:
        print(-1)
elif(a*b<=0 and a>=0):
    print(a)
elif(a*b<=0 and c>=0):
    print(abs(a))
else:
    print(-1)
