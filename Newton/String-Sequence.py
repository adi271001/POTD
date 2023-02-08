a = "abcdefghijklmnopqrstuvwxyz"
p = list(map(int, input().strip().split()))
m = {k: l for k, l in enumerate(a, start=1)}
res = [m[k] for k in p]
print("".join(res))
