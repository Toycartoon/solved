n = int(input())
s = input()
t = input()

a, b = 0, 0
for i in range(n):
    if (s[i] == "R" and t[i] == "S") or (s[i] == "S" and t[i] == "P") or (s[i] == 'P' and t[i] == "R"):
        a += 1
    elif (t[i] == "R" and s[i] == "S") or (t[i] == "S" and s[i] == "P") or (t[i] == 'P' and s[i] == "R"):
        b += 1

print(a, b)
