t = int(input())
if t >= 1 and t <= pow(10,4):
    for i in range (t):
        d = -1
        lst = input()
        a,b,c = lst.split(" ")
        a,b,c = int(a),int(b),int(c)
        for j in range(1,pow(10,5)+1):
            if j % 2 == 0 and j >=2:      #Check for even number and greater than 4
                if abs(j) == abs(a-b):
                    if c >= j:
                        break
                    elif c > j:
                        d = c - j
                        break
                    else:
                        d = c + j 
                        break
            else:
                print(j)
                continue
        print(round(d))