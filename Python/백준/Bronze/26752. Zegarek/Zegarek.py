from datetime import datetime as dt, timedelta

n = dt.strptime(input(), "%H %M %S")
print(dt.strftime(n + timedelta(seconds=1), "%H:%M:%S"))
