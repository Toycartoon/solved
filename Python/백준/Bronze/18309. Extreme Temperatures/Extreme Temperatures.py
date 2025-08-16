mn = float('inf')
mx = -float('inf')
while True:
    try:
        s, *a = input().split()
        a = list(map(int, a))

        mx = max(max(a), mx)
        mn = min(min(a), mn)
    except EOFError:
        break

print(mn, mx)
