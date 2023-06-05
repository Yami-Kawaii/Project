lst = list(map(int,input().split()))
n,k = lst[0],lst[1]
for i in range(k):
    if n % 10 == 0:
        n = n/10
    else:
        n -= 1
print(int(n))