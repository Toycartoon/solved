d = False
w = 1
for i in range(int(input())):
    a, b, m = map(int, input().split())
    w = w // a * b
    if m == 1:
        d = not d
print(int(d), w)
