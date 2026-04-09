n = int(input())
r = list(map(int, input().split()))

v = 0
mx = 0
for i in range(n):
    if mx >= r[i]:
        r[i] = mx
    else:
        mx = r[i]
    v += r[i]

if v % 3 == 0:
    print("Delicious!")
else:
    print("Oh My God!")
