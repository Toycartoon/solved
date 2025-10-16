w = {"Bessie": 0, "Elsie": 0, "Daisy": 0, "Gertie": 0, "Annabelle": 0, "Maggie": 0, "Henrietta": 0}
for _ in range(int(input())):
    s, n = input().split()
    w[s] += int(n)

a = list(w.items())
a.sort(key=lambda x: x[1])

v = sorted(list(set(w.values())))
if len(v) <= 1 or list(w.values()).count(v[1]) > 1:
    print("Tie")
    exit()

for i in a:
    if i[1] == v[1]:
        print(i[0])
        break
