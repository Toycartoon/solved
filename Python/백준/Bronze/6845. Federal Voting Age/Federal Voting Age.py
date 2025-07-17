from datetime import datetime as dt

v = dt(2007, 2, 27)
for i in range(int(input())):
    y, m, d = map(int, input().split())
    t = dt(y, m, d)
    
    print("Yes" if (v - t).days >= 6574 else "No")
