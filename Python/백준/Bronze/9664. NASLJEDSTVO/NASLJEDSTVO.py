n = int(input())
o = int(input())
ans = 1
while True:
    if ans - (ans // n) == o:
        if o % (n-1) == 0:
            print(ans, ans+1)
        else:
            print(ans, ans)
        break
    ans += 1
