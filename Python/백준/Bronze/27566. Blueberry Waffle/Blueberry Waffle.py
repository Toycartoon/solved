r, f = map(int, input().split())
print("up" if (f-(r // 2)) // r % 2 == 1 else "down")
