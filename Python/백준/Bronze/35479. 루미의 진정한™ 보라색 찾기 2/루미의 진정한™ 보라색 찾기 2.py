r, g, b = map(int, input().split())

r_, g_, b_ = r / 255, g / 255, b / 255
k = 1 - max(r_, g_, b_)
c, m, y = 0, 0, 0
if k != 1:
    c = (1 - r_ - k) / (1 - k)
    m = (1 - g_ - k) / (1 - k)
    y = (1 - b_ - k) / (1 - k)
print(c, m, y, k)
