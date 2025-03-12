def prog02():
    #Display all numbers, showing duplicates only once.
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
    
    # Display first occurrence of each number
    seen = set()
    print("\nNumbers (showing first entry of duplicates only):")
    for num in numbers:
        if num not in seen:
            print(num)
            seen.add(num)

#result
prog02()