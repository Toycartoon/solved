n = int(input())
s = list(map(int, input().split()))

o, e = 0, 0
for i in s:
    if i % 2 == 0:
        e += 1
    else:
        o += 1

ans = 0
if o > e:
    ans += 1
elif e > o:
    ans += 2

while True:
    if ans not in s:
        print(ans)
        break
    ans += 2
