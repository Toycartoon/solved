n = int(input())
w = input().split()

ans = 0
diff = 0
for i in range(1, n):
    if int(w[i-1]) > int(w[i]):
        diff += int(w[i-1]) - int(w[i])
    else:
        ans = max(ans, diff)
        diff = 0
print(max(ans, diff))
