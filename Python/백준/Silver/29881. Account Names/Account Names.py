w = {}
v = {}
for i in range(int(input())):
    first, last = input().split()
    w[last] = first

for i in range(len(w)):
    first, account = input().split()
    v[first] = account

for i in w.keys():
    print(i, v[w[i]])
