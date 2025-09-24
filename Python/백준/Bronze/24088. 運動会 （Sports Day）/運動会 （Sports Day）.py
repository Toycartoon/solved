n = int(input())
k = int(input())
s = input()

r = k
w = n-k
for i in s:
    if i == "R":
        r -= 1
    elif i == "W":
        w -= 1

if r > 0:
    print("R")
elif w > 0:
    print("W")
