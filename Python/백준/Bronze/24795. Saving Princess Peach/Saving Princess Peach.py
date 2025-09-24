n, y = map(int, input().split())
a = [True for _ in range(n)]
for i in range(y):
    a[int(input())] = False

for i in range(len(a)):
    if a[i]:
        print(i)
print(f"Mario got {a.count(False)} of the dangerous obstacles.")
