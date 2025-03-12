# Prompt the user to enter the numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Determine the smaller and larger number
start = min(num1, num2)
end = max(num1, num2)

# Loop through the numbers between the two numbers (exclusive)
for i in range(int(start) + 1, int(end)):
    # Print each number followed by a space
    print(i, end=' ')

# Print a newline character at the end
print()