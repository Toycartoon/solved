n, s = input().split()
a = int(input())

s = int(s.replace("?", "9"))
if s >= a:
    print(s)
else:
    print(-1)
