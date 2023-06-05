t = int(input())
if t >= 1 and t <= pow(10,4):
    for i in range (t):
        d = -1
        lst = input()
        a,b,c = lst.split(" ")
        a,b,c = int(a),int(b),int(c)
        for j in range(1,(pow(10,4)+1)):
            n = 2 * abs(a-b)
            if a > n or b > n or c > n:
                print(d)
            else:
                d = n /2 + c
                while d > c:
                    d -= n
            print(d)