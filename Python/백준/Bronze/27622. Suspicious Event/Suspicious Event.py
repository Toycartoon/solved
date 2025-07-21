n = int(input())
a = list(map(int, input().split()))

s = set()
ans = 0
for i in a:
    if i > 0:
        s.add(i)
    elif i < 0:
        if -i in s:
            s.remove(-i)
        else:
            ans += 1

print(ans)
