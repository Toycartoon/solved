from math import gcd

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

i = 1
j = 1
for v in a:
    i *= v

for v in b:
    j *= v

ans = str(gcd(i, j))
if len(ans) >= 10:
    print(ans[-9:])
else:
    print(ans)
