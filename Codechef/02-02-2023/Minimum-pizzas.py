Question Link: https://www.codechef.com/problems/MINPIZZA
    
k = int(input())
for k1 in range(k):
	(p, y) = map(int, input().split(' '))
	piz = p * y // 4
	if p*y % 4 == 0:
	    print(piz)
	else:
	    print(piz+1)
