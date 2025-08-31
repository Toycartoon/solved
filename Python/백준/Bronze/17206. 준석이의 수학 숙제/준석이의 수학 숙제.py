t = int(input())
a = list(map(int, input().split()))
for i in a:
    s, c, yi = i // 3, i // 7, i // 21
    print((s * (6 + (s-1) * 3)) // 2 + (c * (14 + (c-1) * 7)) // 2 - (yi * (42 + (yi-1) * 21)) // 2)
