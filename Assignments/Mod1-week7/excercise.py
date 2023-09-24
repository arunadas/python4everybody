largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = float(num)       # convert input to float
    except:
        print('Invalid input')
        continue
    if largest is None or num > largest:
            largest = num
            
    
    if smallest is None or num < smallest:
          smallest = num
    
        

print("Maximum is", int(largest))
print("Minimum is", int(smallest))