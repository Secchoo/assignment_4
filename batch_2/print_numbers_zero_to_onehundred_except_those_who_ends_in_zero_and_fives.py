# Initialize the counter variable to 0
i = 0

while i <= 100:  # Loop from 0 to 100 inclusive

    if i % 10 != 0 and i % 10 != 5:  # Check if the number does not end in 0 or 5
        print(i, end=' ')  
    i += 1  # Increment the counter variable by 1

print()  