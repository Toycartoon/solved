s, c, o, n = map(int, input().split())

sn, co = s + n, c + o * 2
print(min(sn // 3, co // 6))
