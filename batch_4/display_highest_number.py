#Find the highest number entered.
highest_num = None
    
print("Enter numbers (invalid input to stop):")
while True:
    try:
        num = int(input("Number: "))
        if highest_num is None or num > highest_num:
            highest_num = num
    except ValueError:
        break
    
    if highest_num is not None:
        print(f"\nHighest number entered: {highest_num}")
    else:
        print("\nNo valid numbers entered.")