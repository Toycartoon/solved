p = int(input())
a = [0 for _ in range(100)]
n = int(input())
for i in range(n):
    x, c = input().split()
    if c == "L":
        for j in range(int(x)-1):
            a[j] += 1
    elif c == "R":
        for j in range(int(x), len(a)):
            a[j] += 1

moon, hong, an = 0, 0, 0
for i in a:
    if i % 3 == 0:
        moon += 1
    elif i % 3 == 1:
        hong += 1
    else:
        an += 1

print(f"{p * moon / (moon + hong + an):.02f}")
print(f"{p * hong / (moon + hong + an):.02f}")
print(f"{p * an / (moon + hong + an):.02f}")