x, y = map(int, input().split())
d = int(input())

a = (x * 100 + y - 2 * d) // 4
b = a + d

print(b // 100, b % 100)
print(a // 100, a % 100)
