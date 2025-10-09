ans = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    if a * b < 0:
        if b < 0:
            ans += b-a+1
        else:
            ans += b-a-1
    else:
        ans += b-a
print(ans if ans < 0 else ans + 1)
