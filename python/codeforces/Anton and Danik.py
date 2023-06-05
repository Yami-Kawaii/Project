n = int(input())
s = input()
counter = 0
for i in (s):
    if i == "D":
        counter -= 1
    elif i == "A":
        counter += 1
if counter > 0:
    print("Anton")
elif counter < 0:
    print("Danik")
else:
    print("Friendship")
