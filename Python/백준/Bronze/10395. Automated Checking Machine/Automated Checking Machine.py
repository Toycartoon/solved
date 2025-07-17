a = list(map(int, input().split()))
b = list(map(int, input().split()))

f = True
for i in range(len(a)):
    if a[i] + b[i] != 1:
        f = False
        break

print("Y" if f else "N")
