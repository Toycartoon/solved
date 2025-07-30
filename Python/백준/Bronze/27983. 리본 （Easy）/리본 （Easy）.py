n = int(input())
x = list(map(int, input().split()))
l = list(map(int, input().split()))
c = input().split()

for i in range(n):
    for j in range(n):
        if i == j:
            continue

        if abs(x[i]-x[j]) <= l[i]+l[j] and c[i] != c[j]:
            print("YES")
            print(i+1, j+1)
            exit()

print("NO")
