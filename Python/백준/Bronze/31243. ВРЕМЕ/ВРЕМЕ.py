a = []
for i in range(3):
    sh, sm, eh, em = map(int, input().split())
    m = em - sm
    if m < 0:
        eh -= 1
        m += 60

    h = eh - sh
    if h < 0:
        h += 24
    a.append((h, m))

print(f"{min(a)[0]}:{str(min(a)[1]).zfill(2)}")
print(f"{max(a)[0]}:{str(max(a)[1]).zfill(2)}")
