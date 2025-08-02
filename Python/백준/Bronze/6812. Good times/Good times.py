n = int(input())
t = [n, n-300, n-200, n-100, n, n+100, n+130]
a = ["Ottawa", "Victoria", "Edmonton", "Winnipeg", "Toronto", "Halifax", "St. John\'s"]

for i in range(len(t)):
    if t[i] < 0:
        t[i] += 2400
    if t[i] % 100 >= 60:
        t[i] += 40
    if t[i] > 2359:
        t[i] -= 2400
    print(f"{t[i]} in {a[i]}")
