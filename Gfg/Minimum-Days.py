Question Link:
  
c=0
for k in range(len(S)-1):
  if(S[k]==S[k+1]):
    c+=1
S=list(S)
if c==0:
  return 0
for k in range(N):
  ind=P[k]
  if(ind !=0 and S[ind]==S[ind-1]):
    c-=1
  if(ind!=N-1 and S[ind]==S[ind+1]):
    c-=1
  if(c==0):
    return k+1
  S[ind]='?'
 return -1
