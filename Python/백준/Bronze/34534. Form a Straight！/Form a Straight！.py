a = list(map(int, input().split()))
ans = 5
for i in range(1, 6):
    ans = min(ans, len(set(a) - {*range(i, i+5)}))
print(ans)
