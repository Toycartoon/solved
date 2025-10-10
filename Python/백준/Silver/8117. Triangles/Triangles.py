from itertools import combinations as comb

a = []
while True:
    n = int(input())
    if n == 0:
        break
    a.append(n)

for i, j, k in comb(a, 3):
    if i < j + k and j < i + k and k < i + j:
        print(i, j, k)
        exit()
print("NIE")
