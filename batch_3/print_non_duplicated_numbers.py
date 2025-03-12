def prog01():
    #display numbers with no duplicates
    numbers = []
    
    print("Enter 10 numbers:")
    for i in range(10):
        while True:
            try:
                # Prompt the user to enter a number
                num = int(input(f"Number {i + 1}: "))
                # Add the number to the list
                numbers.append(num)
                break
            except ValueError:
                # Handle invalid input
                print("Invalid input. Please enter a valid number.")
    
    #display unique numbers
    seen = {}
    for num in numbers:
        seen[num] = seen.get(num, 0) + 1
    
    print("\nNumbers with no duplicate:")
    for num in numbers:
        if seen[num] == 1:
            print(num)

#result
prog01()
