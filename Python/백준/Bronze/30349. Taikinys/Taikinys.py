n, m = map(int, input().split())
a, b = map(int, input().split())
x, y = map(int, input().split())

ans = float('inf')
for ty in range(n+1):
    for tx in range(m+1):
        if 0 <= x+tx < a and 0 <= y+ty < b:
            ans = min(ans, x+tx+y+ty)
print(ans if ans != float('inf') else "NEPATAIKYS")
