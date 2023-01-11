Question Link:

t=int(input())
for i in range(t):
    s=input()
    if(s.count('1')>s.count('0')):
        print('WIN')
    else:
        print('LOSE')
