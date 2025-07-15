n = int(input())
s = input().split()

print(s[0][0], end="")
for i in range(1, n):
    if len(s[i-1]) > len(s[i]):
        print(" ", end="")
    else:
        print(s[i][len(s[i-1])-1], end="")
