a = int(input())
b = int(input())

if (a-b) % 360 < (b-a) % 360:
    print(-((a-b) % 360))
else:
    print((b-a) % 360)
