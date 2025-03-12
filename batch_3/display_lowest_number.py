def prog04():
    #Continuously prompt for numbers until invalid input
    min_num = None
    
    print("Enter numbers (invalid input to stop):")
    while True:
        try:
            num = int(input("Number: "))
            if min_num is None or num < min_num:
                min_num = num
        except ValueError:
            if min_num is not None:
                print(f"\nLowest number entered: {min_num}")
            else:
                print("\nNo valid numbers entered.")
            break

#result
prog04()