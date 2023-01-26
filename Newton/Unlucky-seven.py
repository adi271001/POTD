Question Link: https://my.newtonschool.co/playground/code/fiaj9dkknvn7
    
p = int(input())
k = 0
for l in range(1, p+1):
    if '7' not in str(l) and '7' not in oct(l):
        k += 1
print(k)
