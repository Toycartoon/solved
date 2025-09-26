a = list(map(int, input().split()))
l = [0]
v = 0
for i in a:
    v += i
    l.append(v)

for i in range(5):
    for j in range(5):
        print(abs(l[i]-l[j]), end=" ")
    print()
