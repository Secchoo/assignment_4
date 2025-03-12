#Sort numbers in descending order.
numbers = []
    
# Prompt the user to enter numbers until an invalid input is entered
print("Enter numbers (invalid input to stop):")
while True:
    try:
        # Try to convert the input to a float and add it to the list
        num = float(input("Number: "))
        numbers.append(num)
    except ValueError:
        # Break the loop if the input is not a valid float
        break

# Check if any numbers were entered
if numbers:
    print("\nNumbers in descending order:")
    # Sort the numbers in descending order and print them
    for n in sorted(numbers, reverse=True):
        print(n)
else:
    # Inform the user that no valid numbers were entered
    print("\nNo valid numbers entered.")