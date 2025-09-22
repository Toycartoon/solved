n = int(input())
w = [0 for _ in range(53)]
a = list(map(int, input().split()))
for i in a:
    w[i] += 1

s = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
f = True
for i in input():
    if w[s.index(i)] > 0:
        w[s.index(i)] -= 1
    else:
        f = False
        break

if f:
    print("y")
else:
    print("n")
