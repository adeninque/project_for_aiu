l = [2, 176, 135]
res = []
for i in l:
    if i == 0:
        res.append(0)
    else:
        res.append((round((i * 100) / 255)) / 100)
print(res)