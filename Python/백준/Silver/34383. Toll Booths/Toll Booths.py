ans = 0
m = 0
for i in range(int(input())):
    a, n = input().split()
    if a == "T":
        if m < int(n):
            ans += int(n) - m
            m = 0
        else:
            m -= int(n)
    elif a == "G":
        m += int(n)
print(ans)