m, n = map(int, input().split())
team = []

for i in range(m):
    x, y, r, s = map(int, input().split())
    team.append((x, y, r, s, i))

ans = 0
miss = False
for k in range(n):
    tx, ty = map(int, input().split())

    if miss:
        miss = not miss
        continue

    miss = True
    can_kick = []
    for x, y, r, s, i in team:
        if ((tx - x) ** 2 + (ty - y) ** 2) ** 0.5 <= r:
            can_kick.append((s, i))
            miss = False

    if miss:
        continue
    elif sorted(can_kick, key=lambda v: (-v[0]))[0][1] == 0:
        ans += 1
print(ans)
