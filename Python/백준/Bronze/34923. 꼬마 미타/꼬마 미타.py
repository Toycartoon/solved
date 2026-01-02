broken_h, broken_m = map(int, input().split(":"))
h, m = map(int, input().split(":"))

cw, ccw = 0, 0
dcw_m, dcw_h = broken_m, broken_h
dccw_m, dccw_h = broken_m, broken_h
while dcw_m != m or dcw_h != h:
    cw += 1
    dcw_m += 1
    if dcw_m >= 60:
        dcw_h += 1
        dcw_m = 0
    if dcw_h > 12:
        dcw_h = 1

while dccw_m != m or dccw_h != h:
    ccw += 1
    dccw_m -= 1
    if dccw_m < 0:
        dccw_h -= 1
        dccw_m = 59
    if dccw_h <= 0:
        dccw_h = 12

print(min(cw, ccw) * 6)
