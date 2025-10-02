d = list(map(int, [*input()]))
while True:
    try:
        a = list(map(int, [*input()]))
        for i in range(len(a)):
            d[i] = (d[i] + a[i]) % 10
    except EOFError:
        break
print(*d, sep="")
