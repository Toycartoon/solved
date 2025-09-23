w, p = map(int, input().split())
l = [0] + list(map(int, input().split())) + [w]

a = set()
for i in range(len(l)-1):
    for j in range(i+1, len(l)):
        a.add(l[j]-l[i])
print(*sorted(list(a)))
