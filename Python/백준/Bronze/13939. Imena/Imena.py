n = int(input())
s = input().replace("!", ".").replace("?", ".").split(".")

for i in s[:-1]:
    ans = 0
    for v in i.split():
        if v == v.capitalize() and v.isalpha():
            ans += 1
    print(ans)
