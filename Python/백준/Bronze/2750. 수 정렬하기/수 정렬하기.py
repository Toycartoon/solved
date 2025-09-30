num = int(input())
N = []

for i in range(num):
    N.append(int(input()))

for i in range(num-1):
    list_min = i
    for j in range(i+1, num):
        if N[j] < N[list_min]:
            list_min = j

    N[list_min], N[i] = N[i], N[list_min]

for i in range(num):
    print(N[i])