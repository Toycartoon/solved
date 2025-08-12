n = int(input()) + 1
while True:
    if len({*str(n)}) == len(str(n)):
        print(n)
        break
    n += 1
