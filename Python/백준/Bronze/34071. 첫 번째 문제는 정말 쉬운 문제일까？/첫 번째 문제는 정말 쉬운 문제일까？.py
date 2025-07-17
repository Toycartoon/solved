n = int(input())
x = []

for i in range(n):
    x.append(int(input()))

if x[0] == max(x):
    print("hard")
elif x[0] == min(x):
    print("ez")
else:
    print("?")
