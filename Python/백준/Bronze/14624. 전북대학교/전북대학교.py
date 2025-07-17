n = int(input())
if n % 2 == 0:
    print("I LOVE CBNU")
    exit()

print("*" * n)
print(" " * (n // 2) + "*")
for i in range(n // 2 - 1, -1, -1):
    print(" " * i + "*" + " " * (2 * (n // 2 - i) - 1) + "*")
