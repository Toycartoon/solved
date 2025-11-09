ans = 0
for i in range(int(input())):
    s, c, a, r = map(int, input().split())
    if s >= 1000 or c >= 1600 or a >= 1500 or (r != -1 and r <= 30):
        ans += 1
print(ans)
