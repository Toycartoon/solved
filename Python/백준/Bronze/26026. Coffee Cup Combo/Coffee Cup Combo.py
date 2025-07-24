n = int(input())
s = input()

ans = 0
c = 0
for i in s:
    if i == "1":
        c = 2
        ans += 1
    elif i == "0":
        if c >= 1:
            c -= 1
            ans += 1

print(ans)
