n = int(input())
s = ""
for i in range(n):
    s += input()

s = eval(s)
s.sort(key=lambda x: (-x['score'], x['name']))

idx = 1
bm = s[0]['score']
for i in range(n):
    if bm != s[i]['score']:
        bm = s[i]['score']
        idx = i+1
    if s[i]['isHidden'] == 1:
        continue
    print(idx, s[i]['name'], s[i]['score'])
