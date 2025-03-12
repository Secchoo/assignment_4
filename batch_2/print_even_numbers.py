# Initialize the count of even numbers to 0
even_count = 0

# Loop to get 10 numbers from the user
for i in range(10):
    # Prompt the user to enter a number
    num = int(input(f"Enter number {i+1}: "))
    
    # Check if the number is even
    if num % 2 == 0:
        # Increment the count of even numbers
        even_count += 1
    
# Print the count of even numbers entered by the user
print(f"Number of even numbers: {even_count}")