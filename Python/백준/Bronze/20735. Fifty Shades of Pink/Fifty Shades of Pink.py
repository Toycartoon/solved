ans = 0
for i in range(int(input())):
    s = input().lower()
    if "pink" in s or "rose" in s:
        ans += 1

if ans == 0:
    print("I must watch Star Wars with my daughter")
else:
    print(ans)
