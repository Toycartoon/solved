k = int(input())
w = int(input())
h = int(input())
t = int(input())

for _ in range(h):
    for i in range(t):
        print("*" * (k * w + (t * (w+1))))

    for i in range(k):
        for j in range(w):
            print("*" * t + "." * k, end="")
        print("*" * t)

for i in range(t):
    print("*" * (k * w + (t * (w+1))))
