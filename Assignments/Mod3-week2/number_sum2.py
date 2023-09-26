import re

fname = input('Enter file name: ')
fh = open(fname)

numlist = [int(re.findall('[0-9]+', line)[0]) for line in fh]

print(numlist)


