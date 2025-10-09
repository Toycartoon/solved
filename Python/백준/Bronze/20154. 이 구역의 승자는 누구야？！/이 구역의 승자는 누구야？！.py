w = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]
s = input()
a = []
for i in s:
    a.append(w[ord(i)-65])

while len(a) > 1:
    x = []
    for i in range(1, len(a), 2):
        x.append((a[i-1] + a[i]) % 10)

    if len(a) % 2 == 1:
        x.append(a[-1])
    a = x

print("I'm a winner!" if a[0] % 2 == 1 else "You're the winner?")
