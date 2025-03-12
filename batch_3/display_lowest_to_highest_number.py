def prog05():
    """Continuously prompt for numbers until invalid input, sort and display."""
    numbers = []
    
    print("Enter numbers (invalid input to stop):")
    while True:
        try:
            num = int(input("Number: "))
            numbers.append(num)
        except ValueError:
            if numbers:
                print("\nNumbers in ascending order:")
                for n in sorted(numbers):
                    print(n)
            else:
                print("\nNo valid numbers entered.")
            break

#result
prog05()