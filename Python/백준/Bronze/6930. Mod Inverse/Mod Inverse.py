n = int(input())
m = int(input())
try:
    print(pow(n, -1, m))
except ValueError:
    print("No such integer exists.")
