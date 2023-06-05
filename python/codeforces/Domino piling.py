import math
data = list(map(int,input().split(" ")))
save = 0
M,N = data[0],data[1]
if M >= 1 and N >= M and 16 >= N:
    for i in range(1,17):
        print(math.floor(i/2))