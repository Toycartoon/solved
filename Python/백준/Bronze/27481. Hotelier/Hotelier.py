n = int(input())
s = input()

ans = [0 for _ in range(10)]
for i in s:
    if i == "L":
        for x in range(10):
            if ans[x] == 0:
                ans[x] = 1
                break
    elif i == "R":
        for x in range(9, -1, -1):
            if ans[x] == 0:
                ans[x] = 1
                break
    else:
        ans[int(i)] = 0

print(*ans, sep="")
