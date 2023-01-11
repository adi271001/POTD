Question Link: https://www.codechef.com/problems/REPEAT

T = int(input())
for _ in range(T):
    [n, k, s] = map(int, input().split())
    elements = n + k -1
    sum_of_n_odd = n**2
    a = abs(s - sum_of_n_odd)//(k-1)
    print(a)
