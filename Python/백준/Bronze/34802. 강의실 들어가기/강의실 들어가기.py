nh, nm, ns = map(int, input().split(":"))
sh, sm, ss = map(int, input().split(":"))
t, k = map(int, input().split())

now = nh * 3600 + nm * 60 + ns
start = sh * 3600 + sm * 60 + ss
print(int(now + (100 - k) * t // 100 <= start))
