N = int(input())
As = list(map(int, input().split()))
for k in range(N):
    shift = 3**k
    for t in range(3**N):
        if (t // shift) % 3 != 0:
            continue
        s0 = t
        s1 = t + shift
        s2 = t + 2 * shift
        As[s0], As[s1], As[s2] = (
            As[s1] - As[s2],
            As[s0] + As[s2] - As[s1],
            As[s1] - As[s0],
        )
 
print(*As)
