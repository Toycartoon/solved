import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

s = sum(a)
mx = s + min(a) + max(a)
a = list(enumerate(a))

ans = tuple(a)
a.sort(key=lambda x: x[1], reverse=True)
for i in range(n-1):
    v = a.pop()
    s -= v[1]
    if s + a[-1][1] + a[0][1] > mx:
        mx = s + a[-1][1] + a[0][1]
        ans = tuple(a)

print(len(ans))
for i in ans:
    print(i[0]+1, end=" ")
