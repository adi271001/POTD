Question Link: https://my.newtonschool.co/playground/code/vdbw5lxgrsc4
    
def smallest_non_negative(n, sequence):
    num_set = set(sequence)
    for i in range(0, max(sequence)+1):
        if i not in num_set:
            return i
    return max(sequence)+1
n=int(input())
sequence=list(map(int,input().split()))
print(smallest_non_negative(n,sequence))
