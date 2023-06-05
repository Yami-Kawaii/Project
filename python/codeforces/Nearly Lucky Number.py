n = input()
check=False
lucky = 0
unlucky = 0

for i in n:
    if i != "4" and i != "7":
        unlucky += 1
    else:
        lucky += 1

for j in str(lucky):
    if j != "4" and j != "7":
        check = True

if check == False:
    print("YES")
else:
    print("NO")