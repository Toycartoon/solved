ans = 0
for i in range(int(input())):
    ans += max(0, max(list(map(int, input().split()))))

print(ans)
