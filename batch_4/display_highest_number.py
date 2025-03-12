#Find the highest number entered.
numbers = []
    
print("Enter numbers (invalid input to stop):")

# Continuously prompt the user for input
while True:
    try:
        # Try to convert the input to an integer
        num = int(input("Input Number: "))
        # If successful, append the number to the list
        numbers.append(num)
    except ValueError:
        # If a ValueError occurs, it means the input was not a valid integer
        if numbers:
            # If the list is not empty, print the highest number
            print(f"\nHighest number entered: {max(numbers)}")
        else:
            # If the list is empty, inform the user that no valid numbers were entered
            print("\nNo valid numbers entered.")
        # Break out of the loop
        break