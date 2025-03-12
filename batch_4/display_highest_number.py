#Find the highest number entered.
numbers = []
    
print("Enter numbers (invalid input to stop):")
while True:
    try:
        num = float(input("Number: "))
        numbers.append(num)
    except ValueError:
        if numbers:
            print(f"\nHighest number entered: {max(numbers)}")
        else:
            print("\nNo valid numbers entered.")
        break