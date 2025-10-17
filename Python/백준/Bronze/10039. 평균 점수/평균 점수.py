all_score = 0
each_score = 0

for i in range(5):
    each_score = int(input())
    if each_score < 40:
        each_score = 40
    all_score += each_score

print(int(all_score / 5))