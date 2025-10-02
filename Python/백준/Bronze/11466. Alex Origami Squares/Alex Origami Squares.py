h, w = map(int, input().split())
print(max(min(h, w) / 2, min(max(h, w) / 3, min(h, w))))
