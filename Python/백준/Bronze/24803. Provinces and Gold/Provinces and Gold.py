g, s, c = map(int, input().split())
cost = 3 * g + 2 * s + c

if cost >= 8:
    print("Province or ", end="")
elif cost >= 5:
    print("Duchy or ", end="")
elif cost >= 2:
    print("Estate or ", end="")

if cost >= 6:
    print("Gold")
elif cost >= 3:
    print("Silver")
else:
    print("Copper")
