d = int(input())
a, o = map(int, input().split())
da, do = map(int, input().split())

ans = max(0, a-d*da) / max(1, a-d*da+o-d*do) * 100
if ans < 0:
    print(0)
elif ans > 100:
    print(100)
else:
    print(ans)
