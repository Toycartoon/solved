n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in a:
    if str(i) == str(i)[::-1]:
        ans += i

print(ans)
