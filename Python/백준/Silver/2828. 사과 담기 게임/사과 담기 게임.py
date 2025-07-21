n, m = map(int, input().split())
j = int(input())
l, r = 0, m

ans = 0
for i in range(j):
    a = int(input())
    if r < a:
        ans += a-r
        r = a
        l = r - m
    elif a <= l:
        ans += l-a+1
        l = a-1
        r = l + m

print(ans)
