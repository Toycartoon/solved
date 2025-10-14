p, n = map(int, input().split())
a = [0 for _ in range(p+1)]

def change_sequence(s, opp):
    idx = s
    for j in range(s-1, 0, -1):
        if a[j] == 0:
            break
        elif a[j] == opp:
            idx = j
            break
    for j in range(idx+1, s):
        a[j] = 0

    idx = s
    for j in range(s+1, p+1):
        if a[j] == 0:
            break
        elif a[j] == opp:
            idx = j
            break
    for j in range(s+1, idx):
        a[j] = 0

for i in range(n):
    s = int(input())
    if i % 2 == 0:
        a[s] = 1
        change_sequence(s, 1)
    else:
        a[s] = 2
        change_sequence(s, 2)
print(a.count(1), a.count(2))
