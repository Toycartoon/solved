n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

ans = 0
for i in a:
    ans += i

    if ans in b:
        ans = 0

print(ans)
