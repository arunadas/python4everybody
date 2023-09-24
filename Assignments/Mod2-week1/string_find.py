text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(':')
spos = text.find(' ', pos)
print(spos)
number = text[spos:]
number = float(number)
print(number)