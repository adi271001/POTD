Question Link: https://www.codechef.com/problems/EZSPEAK

for _ in range(int(input())):
    k = int(input())
    l = input()
    if k<=3:
        print("YES")
    else:
        for m in range(k-3):
            p = l[m:m+4]
            v1 = 'a' in p or 'e' in p or 'i' in p 
            v2 = 'o' in p or 'u' in p 
            if not v1 and not v2:
                print("NO")
                break 
        else:
            print("YES")
