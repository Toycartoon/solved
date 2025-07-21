n, p, s = map(int, input().split())
for i in range(s):
    a, *g = map(int, input().split())
    if p in g:
        print("KEEP")
    else:
        print("REMOVE")
