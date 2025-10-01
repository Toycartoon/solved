n = int(input())
for i in range(1, 8):
    if i * (i + 1) // 2 >= n:
        print(i)
        exit()
print(7 + ((n-22) // 7))
