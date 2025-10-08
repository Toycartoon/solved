s = set()
n = int(input())
for i in range(n):
    s.add(input())

for i in range(int(input())):
    v = input()
    if v in s:
        s.remove(v)

    if len(s) <= n // 2:
        print(i+1)
        break
