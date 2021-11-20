lsf=-1
print('start,',lsf)
for num in [8, 40, 34, 8, 7, 6]:
    if num > lsf:
        lsf = num
    print(lsf, num)

print('finish ',lsf)
