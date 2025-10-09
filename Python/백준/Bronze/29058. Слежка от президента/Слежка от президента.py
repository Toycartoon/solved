n, m, k = map(int, input().split())

clip = []
view = [[] for _ in range(n)]
idx = 0
for i in range(m):
    com = input()
    if com == "Next":
        idx = (idx + 1) % n
    elif com == "Backspace":
        if len(view[idx]) > 0:
            view[idx].pop()
    elif com == "Copy":
        clip = view[idx][-k:]
    elif com == "Paste":
        view[idx].extend(clip)
    else:
        view[idx].append(com)
print(*view[idx][-k:] if len(view[idx]) > 0 else "Empty", sep="")
