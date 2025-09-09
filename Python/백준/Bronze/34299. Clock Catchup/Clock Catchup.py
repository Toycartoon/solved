sh, sm, ss = map(int, input().split(":"))
eh, em, es = map(int, input().split(":"))
print(int(sh < 12 and eh >= 12), (eh-sh), (eh-sh) * 60 + (em - sm))
