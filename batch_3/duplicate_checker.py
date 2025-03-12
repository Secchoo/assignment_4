def prog03():
    #Continuously prompt for numbers until invalid input.
    seen = set()
    
    print("Enter numbers (invalid input to stop):")
    while True:
        try:
            num = float(input("Number: "))
            status = "Unique" if num not in seen else "Duplicate"
            print(status)
            seen.add(num)
        except ValueError:
            print("Done!")
            break

# Example usage
prog03()