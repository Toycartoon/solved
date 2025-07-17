n = int(input())
a = input()
b = input()

w, l = 0, 0
for i in range(n):
    if (a[i] == "R" and b[i] == "S") or (a[i] == "S" and b[i] == "P") or (a[i] == "P" and b[i] == "R"):
        w += 1
    elif (b[i] == "R" and a[i] == "S") or (b[i] == "S" and a[i] == "P") or (b[i] == "P" and a[i] == "R"):
        l += 1

if w > l:
    print("victory")
else:
    print("defeat")
