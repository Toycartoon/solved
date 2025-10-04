t1, t2 = map(int, input().split())
print("O" if (t1 * 12) % 360 == t2 else "X")