a = []
s = 0
for i in range(int(input())):
    n = int(input())
    a.append(n)
    s += n

for i in a:
    if i == s-i:
        print(i)
        exit()

print("BAD")
