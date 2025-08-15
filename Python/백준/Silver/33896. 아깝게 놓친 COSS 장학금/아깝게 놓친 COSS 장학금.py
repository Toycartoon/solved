from math import trunc

a = []
for i in range(int(input())):
    name, score, risk, cost = input().split()
    score, risk, cost = int(score), int(risk), int(cost)
    a.append((name, cost, trunc(score ** 3 / (cost * (risk + 1)))))

a.sort(key=lambda x: (-x[2], x[1], x[0]))
print(a[1][0])
