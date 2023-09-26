import re

fname = input('Enter file name: ')
fh = open(fname)
numlist = []

for line in fh:
    line = line.rstrip()
    num_extract = re.findall('[0-9]+', line)
    
    if len(num_extract) >= 1:
       # print(num_extract)
        numlist.extend([int(num) for num in num_extract])
#print(numlist)
print(sum(numlist))

