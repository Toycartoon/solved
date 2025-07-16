n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = sum(a)
for i in b:
    if i != 0:
        ans *= i

print(ans)
