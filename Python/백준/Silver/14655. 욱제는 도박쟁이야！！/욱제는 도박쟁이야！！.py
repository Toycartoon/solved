n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for i in a + b:
    if i >= 0:
        ans += i
    else:
        ans -= i

print(ans)
