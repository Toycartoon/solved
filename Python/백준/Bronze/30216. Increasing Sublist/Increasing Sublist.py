ans = []
n = int(input())
a = list(map(int, input().split()))

x = 1
for i in range(1, n):
    if a[i] <= a[i-1]:
        ans.append(x)
        x = 0
    x += 1

ans.append(x)
print(max(ans))
