counts=dict()
for x in ['csev', "cwen", "zqian", "cwen"]:
    print(x)
    if x not in counts:
        counts[x] = 1 
    else:
        counts[x] = counts[x] + 1   
print(counts)