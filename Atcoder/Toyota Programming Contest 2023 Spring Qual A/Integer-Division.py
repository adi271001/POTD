mod = 998244353
n = int(input())
dp, sum = [1], [1]
s = '1'+input()
for k in range(1, n+1):
    t = int(s[k])
    if k == 1:
        dp.append(t)
    elif k == 2:
        dp.append(dp[k-1]*t+dp[k-1]*10+t)
    else:
        dp.append(dp[k-1]*t+dp[k-1]*10+sum[k-2]*t)
    dp[k] %= mod
    sum.append((sum[k-1]+dp[k])%mod)
print(dp[n])
