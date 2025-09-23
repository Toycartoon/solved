n = int(input())
swift = list(map(int, input().split()))
sema = list(map(int, input().split()))

sw, se = sum(swift), sum(sema)
for k in range(n-1, -2, -1):
    if sw == se:
        print(k+1)
        break

    sw -= swift[k]
    se -= sema[k]
