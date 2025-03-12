#Calculate average of all numbers.
total = 0
count = 0
    
print("Enter numbers (invalid input to stop):")
while True:
    try:
        num = float(input("Number: "))
        total += num
        count += 1
    except ValueError:
        break
    
if count == 0:
    print("\nNo valid numbers entered.")
else:
    average = total / count
    print(f"\nAverage: {average}")