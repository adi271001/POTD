Question Link: https://www.codechef.com/problems/NUM239

k = int(input())
if(k >= 1 and k <= 100):
    for _ in range(k):
        li, rs = map(int, input().split())
        co = 0
        if li >= 1 and li <= rs and rs <= (pow(10, 5)):
            for m in range(li, rs+1, 1):
                if m%10==2 or m%10==3 or m%10==9:
                    co+=1
            print(co)
