import sys

input = sys.stdin.readline

min_l, min_mid, min_r = 0, 0, 0
max_l, max_mid, max_r = 0, 0, 0
for i in range(int(input())):
    a = list(map(int, input().split()))
    if i == 0:
        min_l, min_mid, min_r = a
        max_l, max_mid, max_r = a
    else:
        min_l, min_mid, min_r = a[0] + min(min_l, min_mid), a[1] + min(min_l, min_mid, min_r), a[2] + min(min_mid, min_r)
        max_l, max_mid, max_r = a[0] + max(max_mid, max_l), a[1] + max(max_l, max_mid, max_r), a[2] + max(max_mid, max_r)
print(max(max_l, max_mid, max_r), min(min_l, min_mid, min_r))
