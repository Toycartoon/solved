a, b = map(int, input().split())

if a - b > a // 2 or a - b <= 0:
    print("NO")
    exit()

print("YES")
print(a - b)
while a - b > 1:
    print("aba")
    a -= 2
    b -= 1

print("ab" * b + "a")
