h, w, w1, w2 = map(float, input().split())
print(w * w1 + (w1 + w2) * h + ((w2-w1) ** 2 + h ** 2) ** 0.5 * w)