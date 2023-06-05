t = int(input())
for _ in range(t):
    counter = 0
    lst = list(map(int,input().split(" ")))
    a,b,n = lst[0],lst[1],lst[2]
    while b <= n:
        b += a
        counter += 1
    print(counter)