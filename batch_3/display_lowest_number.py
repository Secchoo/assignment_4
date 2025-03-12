def prog04():
    #Continuously prompt for numbers until invalid input
    min_num = None
    
    print("Enter numbers (invalid input to stop):")
    while True:
        try:
            num = int(input("Number: "))
            # Update min_num if it's the first number or if the new number is lower
            if min_num is None or num < min_num:
                min_num = num
        except ValueError:
            # If input is invalid, check if any valid numbers were entered
            if min_num is not None:
                print(f"\nLowest number entered: {min_num}")
            else:
                print("\nNo valid numbers entered.")
            # Exit the loop on invalid input
            break

#result
prog04()