y = str(input())

while True:
    counter = 0
    y += 1
    for i in range(0,10):
        if str(i) in str(y):
            counter+=1
    if counter == 4:
        print(y)
        break