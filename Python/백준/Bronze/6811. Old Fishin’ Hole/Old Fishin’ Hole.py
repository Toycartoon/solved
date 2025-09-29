from math import ceil

trout = int(input())
pike = int(input())
pickerel = int(input())
score = int(input())
ans = 0
for i in range(ceil(score / trout)+1):
    for j in range(ceil(score / pike)+1):
        for k in range(ceil(score / pickerel)+1):
            if i == j == k == 0:
                continue
            if i * trout + j * pike + k * pickerel <= score:
                print(f"{i} Brown Trout, {j} Northern Pike, {k} Yellow Pickerel")
                ans += 1
print(f"Number of ways to catch fish: {ans}")
