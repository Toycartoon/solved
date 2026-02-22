ax, ay = map(float, input().split())
bx, by = map(float, input().split())
cx, cy = map(float, input().split())
r = float(input())

a = ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5
b = ((bx - cx) ** 2 + (by - cy) ** 2) ** 0.5
c = ((cx - ax) ** 2 + (cy - ay) ** 2) ** 0.5

v = (0.25 * (4 * a ** 2 * b ** 2 - (a ** 2 + b ** 2 - c ** 2) ** 2) ** 0.5) * 2 / (a + b + c)
print((v-r) / r * 100)
