# x=open('mbox.txt')
# # x='dhnamvn127'
# count=0
# for cheese in x:
#     count = count +1
# print('line count:', count)

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line=line.rstrip()
#     if not '@uct.ac.za' in line :
#         continue
#     print(line)

fname=input('enter the file name:')
fhand=open(fname)
count=0
for line in fhand:
    if line.startswith('Subject:'):
        count=count+1
print('there were', count,'smubsect line in',fname)      