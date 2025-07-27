n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = list(range(1, n+1))
for i in a:
    ans.remove(i)

for i in b:
    ans.remove(i)

print(len(ans))
print(*ans)
