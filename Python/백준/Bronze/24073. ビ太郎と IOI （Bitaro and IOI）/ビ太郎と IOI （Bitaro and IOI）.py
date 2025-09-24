n = int(input())
s = input()
f = False
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if s[i] + s[j] + s[k] == "IOI":
                f = True

if f:
    print("Yes")
else:
    print("No")
