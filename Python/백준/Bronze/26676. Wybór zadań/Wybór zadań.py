n = int(input())
a = input().split()

arr = [[0, 0, 0] for _ in range(5)]
for i in a:
    arr[int(i[0])-1][ord(i[1])-65] += 1

f = True
for i in range(5):
    if (min(arr[i]) < 1 and i != 4) or (i == 4 and min(arr[i]) < 2):
        f = False
        break

if f:
    print("TAK")
else:
    print("NIE")
