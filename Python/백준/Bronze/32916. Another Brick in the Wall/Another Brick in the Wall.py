l, h = map(int, input().split())
if l % 2 == 0 and h % 2 == 1:
    print(h-1)
else:
    print(h)
