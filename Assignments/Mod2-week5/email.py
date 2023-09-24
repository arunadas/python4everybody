name = input("Enter file name: ")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)
count = 0
email_counts = dict()


for line in handle:
    if line.startswith("From "):
        words = line.split()

        email = words[1]
        # create a dictionary with words and its count
        email_counts[email] = email_counts.get(email , 0) + 1
max_email = None
max_count = None

# max loop in dictionary
for email , count in email_counts.items():
    if max_count is None or count > max_count :
        max_count = count
        max_email = email

print(max_email, max_count)        
