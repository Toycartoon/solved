n = int(input())
l = list(map(int, input().split()))

f = False
for k in range(1, n // 2 + 1):
    if l[:k] == l[-k:]:
        f = True
        break
print("yes" if f else "no")
