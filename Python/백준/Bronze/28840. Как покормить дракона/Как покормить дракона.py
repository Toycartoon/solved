from datetime import datetime as dt

a = input()
b = input()

at = dt.strptime(a, "%H:%M")
bt = dt.strptime(b, "%H:%M")

t = bt-at
if t.days == -1:
    print(f"{str(t.seconds // 3600).zfill(2)}:{str(t.seconds % 3600 // 60).zfill(2)}")
else:
    print(f"{str(24 + t.seconds // 3600).zfill(2)}:{str(t.seconds % 3600 // 60).zfill(2)}")
