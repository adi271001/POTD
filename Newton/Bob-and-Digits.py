Question Link: https://my.newtonschool.co/question-of-the-day?leaderboardType=fastest_today
    
def count_digits(n, k):
    count = 0
    while n > 0:
        count += 1
        n //= k
    return count
n, k = map(int, input().split())
print(count_digits(n, k))
