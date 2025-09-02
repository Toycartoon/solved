k = [1, 1, 2, 4]
for i in range(4, 70):
    k.append(k[-1] + k[-2] + k[-3] + k[-4])
for t in range(int(input())):
    print(k[int(input())])
