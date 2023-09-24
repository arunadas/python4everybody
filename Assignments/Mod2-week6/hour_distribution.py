name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
hour_count = dict()


for line in handle:
    if line.startswith('From '):
        words = line.split()
        hour = words[5].split(':')[0]
        #print(hour)
        # build dictionary with hour count
        hour_count[hour] = hour_count.get(hour , 0) + 1
        
for k , v in sorted(hour_count.items()):
    print(k , v)
