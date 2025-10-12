plan = {"Marble": (19, 200), "Marble+": (19, 350), "Quartz": (14, 200), "Quartz+": (14, 350)}
for t in range(int(input())):
    name, p, swipe, money = input().split()
    lefts, leftm = plan[p][0]-int(swipe), plan[p][1]-float(money)
    print(f"{name} {lefts} {leftm:.02f} ", end="")

    if lefts > 0 and leftm > 0:
        print("Use meal swipe or munch money")
    elif leftm > 0:
        print("Use munch money")
    elif lefts > 0:
        print("Use meal swipe")
    else:
        print('Go to Downtown Golden!')
