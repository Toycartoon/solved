k = input()

if len(k) <= 2:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
    exit()

d = int(k[1]) - int(k[0])
f = True

for i in range(1, len(k)):
    if int(k[i-1]) + d != int(k[i]):
        f = False
        break

if f:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    print("흥칫뿡!! <(￣ ﹌ ￣)>")
