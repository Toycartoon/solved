from math import trunc

w = {"R": 0.55, "G": 0.7, "B": 0.8, "Y": 0.85, "O": 0.9, "W": 0.95}
for i in range(int(input())):
    price, d, c, p = input().split()
    price = int("".join(price.split("."))) * w[d]
    if c == "C":
        price *= 0.95

    if p == "P":
        print(f"${price / 100:.02f}")
    else:
        print(f"${trunc(price / 10 + 0.4) / 10:.02f}")
