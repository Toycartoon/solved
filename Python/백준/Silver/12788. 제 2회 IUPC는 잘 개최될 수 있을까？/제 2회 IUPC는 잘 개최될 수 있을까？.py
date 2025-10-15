n = int(input())
m, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)

if sum(a) < m * k:
    print("STRESS")
    exit()

ans = 0
v = m * k
for i in a:
    v -= i
    ans += 1
    if v <= 0:
        break
print(ans)
