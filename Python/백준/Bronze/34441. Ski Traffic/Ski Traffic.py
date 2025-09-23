hill = input()
h, m = map(int, input().split(":"))
t = h * 60 + m
week = input()
i70 = bool(int(input()))
snow = bool(int(input()))
holiday = bool(int(input()))

if week == "sat" or week == "sun":
    t *= 2
if i70:
    t *= 2
if snow:
    t *= 3
if holiday:
    t *= 3

print(f"{t // 60}:{str(t % 60).zfill(2)}")
