pine, berry = 0, 0
x = [-11 for _ in range(9)]
for _ in range(int(input())):
    t, a, b = map(int, input().split())
    if a <= 4:
        pine += 100
        if t-x[a] <= 10:
            pine += 50
    else:
        berry += 100
        if t-x[a] <= 10:
            berry += 50
    x[a] = t
print(pine, berry)
