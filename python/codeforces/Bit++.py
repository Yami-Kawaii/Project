n = int(input())
x = 0
for i in range (n):
    lst = input()
    if lst[0] == "+" and lst[1] == "+" or lst[1] == "+" and lst[2] == "+":
        x += 1
    elif lst[0] == "-" and lst[1] == "-" or lst[1] == "-" and lst[2] == "-":
        x -= 1
print(x)