n = int(input())
a = list(map(int, input().split()))

b = []
for i in a:
    b.append(i)

upper_idx = [-1 for _ in range(n)]
lower_idx = [-1 for _ in range(n)]
for i in range(n):
    upper_idx[a[i]-1] = i
    lower_idx[a[i]-1] = i

upper_ans = 0
lower_ans = 0
for i in range(n):
    if upper_idx[i] != i:
        upper_ans += 1
        j = a[i]-1
        upper_idx[j], upper_idx[i] = upper_idx[i], upper_idx[j]
        a[upper_idx[i]], a[upper_idx[j]] = a[upper_idx[j]], a[upper_idx[i]]
    if lower_idx[i] != n-i-1:
        lower_ans += 1
        j = b[n-i-1]-1
        lower_idx[j], lower_idx[i] = lower_idx[i], lower_idx[j]
        b[lower_idx[i]], b[lower_idx[j]] = b[lower_idx[j]], b[lower_idx[i]]

print(n-2, min(lower_ans, upper_ans))
