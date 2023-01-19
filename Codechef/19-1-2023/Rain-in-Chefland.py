Question Link: https://www.codechef.com/problems/RAINFALL1
    
s = int(input())
for l in range(s):
    a = int(input())
    if (a >= 7):
        print("HEAVY")
    elif (a >= 3):
        print("MODERATE")
    else:
        print("LIGHT")
