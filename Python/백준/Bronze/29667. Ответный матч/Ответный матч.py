a1, b1 = map(int, input().split(":"))
b2, a2 = map(int, input().split(":"))
print("YES" if a1 >= b2 and b1 >= a2 else "NO")
