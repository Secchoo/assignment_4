def prog01():
    #display numbers with no duplicates
    numbers = []
    
    print("Enter 10 numbers:")
    for i in range(10):
        while True:
            try:
                num = int(input(f"Number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    # Count occurrences and display unique numbers
    seen = {}
    for num in numbers:
        seen[num] = seen.get(num, 0) + 1
    
    print("\nNumbers with no duplicate:")
    for num in numbers:
        if seen[num] == 1:
            print(num)

# Example usage
prog01()
