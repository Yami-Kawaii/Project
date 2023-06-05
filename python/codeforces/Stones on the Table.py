word = input()
set_ = set()
for i in word:
    set_.add(i)
if len(set_) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")