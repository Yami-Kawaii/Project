from typing import Counter


x = int(input())
counter = 0
while x != 0:
    if x >=5:
        x -= 5
    else:
        x -= x
    counter += 1
print(counter)