s = input()
n = len(s)
if n % 2 == 1:
    n -= 1

for i in range(n, 0, -2):
    for j in range(i, len(s)+1):
        v = s[j-i:j]
        if sum(map(int, [*v[:len(v)//2]])) == sum(map(int, [*v[len(v)//2:]])):
            print(i)
            exit()
