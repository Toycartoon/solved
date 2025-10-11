from math import ceil

t = 1
while True:
    n = int(input())
    if n == 0:
        break

    print(f"File #{t}")
    print(f"John needs {ceil(n * 3 / 7440000)} floppies.")
    print()

    t += 1
