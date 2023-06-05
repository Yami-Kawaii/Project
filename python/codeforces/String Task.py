n = input()
v = ["A", "O", "Y", "E", "U", "I","a", "o", "y", "e", "u", "i"]
s = ""
for a in n:
    if a in v:
        continue
    else:
        s += f".{a.lower()}"
print(s)