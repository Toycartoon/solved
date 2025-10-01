# Special Thanks : ohwphil

t = 1
while True:
    n, nstar, nbang = map(int, input().split())
    if n == nstar == nbang == 0:
        break

    print(f"Sequence set {t}")
    for mask in range(2 ** n):
        arr = []
        for i in range(n):
            if mask & (1 << i):
                arr.append("!")
            else:
                arr.append("*")

        if "!" * (nbang+1) not in "".join(reversed(arr)) and "*" * (nstar+1) not in "".join(reversed(arr)):
            print(*reversed(arr), sep="")

    t += 1
