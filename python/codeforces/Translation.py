import sys
ymap = list(map(str,input()))
y = int("".join(ymap))
while True:
    for i in range(1,10):
        if ymap.count(str(i)) > 0:
            y += 1
            ymap = list(map(str,str(y)))
            break
    print(y)
    break