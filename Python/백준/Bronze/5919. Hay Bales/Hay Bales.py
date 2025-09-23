n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

s = sum(a) // n
ans = 0
for i in a:
    ans += abs(i-s)
print(ans // 2)
