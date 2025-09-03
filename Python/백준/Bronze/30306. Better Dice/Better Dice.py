n = int(input())
f = list(map(int, input().split()))
s = list(map(int, input().split()))

o, t = 0, 0
for i in f:
    for j in s:
        if i > j:
            o += 1
        elif j > i:
            t += 1

if o > t:
    print("first")
elif o < t:
    print("second")
else:
    print("tie")
