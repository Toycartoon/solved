s = input()
n = int(input())

a = []
for t in range(26):
    v = ""
    for i in s:
        x = ord(i)-t
        if x < 97:
            x += 26
        v += chr(x)
    a.append(v.count("r"))
ans = sum(a) * (n // 26) + sum(a[:n%26])
print(ans)
