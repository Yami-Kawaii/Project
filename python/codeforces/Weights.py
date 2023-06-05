""" 
5
3 8 2 13 7
LLRLL

 """
n = int(input())
a = input().split(" ")
S = list(map(str,input()))
for i in range(n):
    if S[i] == "L":
        print(a[i],"R")
    else:
        print(a[i],"L")