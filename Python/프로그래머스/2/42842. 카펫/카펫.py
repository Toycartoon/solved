def solution(brown, yellow):
    for i in range(1, yellow+1):
        if yellow % i == 0:
            x, y = yellow // i, i
            if (x * 2) + (y * 2) + 4 == brown:
                return x+2, y+2
