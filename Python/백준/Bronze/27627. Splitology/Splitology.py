s = input()
for i in range(1, len(s)):
    a, b = s[:i], s[i:]
    if a == a[::-1] and b == b[::-1]:
        print(a, b)
        exit()
print("NO")
