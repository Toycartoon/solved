n = int(input())
s = ""
for i in range(1, n+1):
    if str(i) not in s:
        s += str(i)

print(s)
