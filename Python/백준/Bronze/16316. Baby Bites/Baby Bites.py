n = int(input())
a = input().split()

f = True
for i in range(n):
    if a[i] != "mumble" and a[i] != str(i+1):
        f = False
        break

print("makes sense" if f else "something is fishy")
