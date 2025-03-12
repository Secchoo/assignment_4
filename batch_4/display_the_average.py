#Calculate average of all numbers.
total = 0
count = 0
    
print("Enter numbers (invalid input to stop):")
while True:
    try:
        # Read user input and convert to float
        num = float(input("Number: "))
        total += num
        count += 1
    except ValueError:
        # Break the loop if input is not a valid number
        break

# Check if any valid numbers were entered
if count == 0:
    print("\nNo valid numbers entered.")
else:
    # Calculate and display the average
    average = total / count
    print(f"\nAverage: {average}")