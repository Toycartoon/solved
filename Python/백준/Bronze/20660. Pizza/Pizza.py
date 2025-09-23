n, *a = map(int, input().split())
ans = 0
for i in range(int(input())):
    k, *b = map(int, input().split())
    if len(set(a) & set(b)) == 0:
        ans += 1
print(ans)
