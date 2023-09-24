fname = input("Enter file name: ")
fh = open(fname)
count = 0
spam_confidence = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos = line.find(':')
    spam_confidence += float(line[pos+1:])
    count += 1
print("Average spam confidence:", spam_confidence/count)