Question Link:
  
a=input()
def find_last_index_of_a(S):
    for i in range(len(S)-1, -1, -1):
        if S[i] == 'a':
            return i + 1
    return -1
print(find_last_index_of_a(a))
