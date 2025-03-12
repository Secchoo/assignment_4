def prog03():
    #Continuously prompt for numbers until invalid input.
    seen = set()
    
    print("Enter numbers (invalid input to stop):")
    while True:
        try:
            num = int(input("Number: "))
            # Check if the number is unique or duplicate
            status = "Unique" if num not in seen else "Duplicate"
            print(status)
            # Add the number to the set of seen numbers
            seen.add(num)
        except ValueError:
            # Handle invalid input and exit the loop
            print("Done!")
            break

#result
prog03()