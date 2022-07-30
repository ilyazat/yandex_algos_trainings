troom, tcond = tuple(map(int, input().split()))
mode = input()
res = 0
if mode == 'freeze':
    if troom > tcond:
        res = tcond
    else:
        res = troom
elif mode == 'heat':
    if troom > tcond:
        res = troom
    else:
        res = tcond
elif mode == 'auto':
    res = tcond
else:
    res = troom
print(res)