p = 100 - int(input())

print(p // 25, end=" ")
p %= 25
print(p // 10, end=" ")
p %= 10
print(p // 5, end=" ")
p %= 5
print(p)
