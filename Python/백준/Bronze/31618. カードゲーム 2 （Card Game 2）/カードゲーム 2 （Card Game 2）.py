n = int(input())
a = set(map(int, input().split()))

f = False
for i in a:
    if i + 3 in a and i + 6 in a:
        f = True
        break
print("Yes" if f else "No")
