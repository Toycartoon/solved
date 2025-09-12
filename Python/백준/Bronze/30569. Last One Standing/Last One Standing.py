h1, d1, t1 = map(int, input().split())
h2, d2, t2 = map(int, input().split())

t = 0
while h1 > 0 and h2 > 0:
    if t % t1 == 0:
        h2 -= d1
    if t % t2 == 0:
        h1 -= d2
    t += 1

if h1 > 0:
    print("player one")
elif h2 > 0:
    print("player two")
else:
    print("draw")
