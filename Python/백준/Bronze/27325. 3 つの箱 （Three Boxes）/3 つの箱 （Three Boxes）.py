n = int(input())
s = input()
x = 1

ans = 0
for i in s:
    if i == "L":
        x = max(1, x-1)
    elif i == "R":
        x = min(3, x+1)

    if x == 3:
        ans += 1

print(ans)
