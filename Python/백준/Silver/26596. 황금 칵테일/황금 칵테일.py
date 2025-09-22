from math import trunc

w = {}
for i in range(int(input())):
    s, x = input().split()
    if s in w:
        w[s] += int(x)
    else:
        w[s] = int(x)

f = False
for i in range(len(w.values())):
    if trunc(list(w.values())[i] * 1.618) in w.values() and (list(w.values()).index(trunc(list(w.values())[i] * 1.618)) != i or list(w.values()).count(trunc(list(w.values())[i] * 1.618)) >= 2):
        f = True
        break

if f:
    print("Delicious!")
else:
    print("Not Delicious...")
