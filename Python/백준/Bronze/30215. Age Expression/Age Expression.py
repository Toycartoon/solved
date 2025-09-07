o, al, ko = map(int, input().split())
f = False
for k in range(1, o // ko + 1):
    if o - (k * ko) > 0 and (o - k * ko) % al == 0:
        f = True
        break
print(int(f))
