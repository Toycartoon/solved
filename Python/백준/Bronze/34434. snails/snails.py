import sys

input = sys.stdin.readline

m = [0, 1, 2, 3]
for i in range(4, 2 ** 15):
    m.append(m[-1] + m[-2] + m[-3] + m[-4])

for i in range(int(input())):
    a = list(map(int, input().split()))
    if m[:len(a)] == a:
        print("NAUTILUS")
    else:
        print("SNAIL")
