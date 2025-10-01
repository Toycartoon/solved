l, g, r = map(int, input().split())
arr = [False for _ in range(l+1)]

w = {}
for i in range(g):
    s, a, d = input().split()
    w[s] = (int(a), int(d))

for _ in range(r):
    s = input()
    a, d = w[s]
    for i in range(a, l+1, d):
        arr[i] = not arr[i]
print(arr.count(True))
