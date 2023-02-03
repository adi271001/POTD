Question Link: https://my.newtonschool.co/playground/code/qtmco3u05r5j
  
def Alexa_and_Balls(A, B, C, D):
    if B >= D * C:
        return -1
    else:
        operation = 1
        while (A + B * operation) / (C  * operation) > D:
            operation += 1
        return operation if operation <= 1000000 else -1

A, B, C, D = map(int, input().split())
print(Alexa_and_Balls(A, B, C, D))
