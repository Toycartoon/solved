n = int(input())
s = input()
if n < len(s):
    print("Impossible")
    exit()

ans = 0
for i in s:
    ans += ord(i) - 96

print(ans)
