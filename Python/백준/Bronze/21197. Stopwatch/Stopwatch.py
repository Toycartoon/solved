stop = True
ans = 0
b = 0
for i in range(int(input())):
    n = int(input())
    if stop:
        b = n
    else:
        ans += n - b
    stop = not stop

if stop:
    print(ans)
else:
    print("still running")
