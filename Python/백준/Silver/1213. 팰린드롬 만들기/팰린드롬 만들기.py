s = input()
g = [0 for _ in range(26)]

for i in s:
    g[ord(i)-65] += 1

odd = -1
for i in range(26):
    if g[i] % 2 == 1:
        if odd == -1:
            odd = i
        else:
            odd = -2

if odd == -2 or (len(s) % 2 == 0 and odd != -1):
    print("I\'m Sorry Hansoo")
    exit()

ans = ""
for i in range(26):
    ans += chr(i+65) * (g[i] // 2)

ans += (chr(odd+65) if len(s) % 2 == 1 else "") + ans[::-1]
print(ans)
