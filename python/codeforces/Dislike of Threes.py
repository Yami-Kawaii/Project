db = []
counter = 1
while len(db) <= 999:
    if counter % 3 != 0 and str(counter)[-1] not in "3":
        db.append(counter)
    counter += 1

t = int(input())
if t >= 1 and t <= 10000:
    for i in range(t):
        k = int(input())
        print(db[k-1])