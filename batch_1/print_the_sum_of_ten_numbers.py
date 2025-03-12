#sum variable
total_sum = 0

#loop to get 10 numbers
for i in range(10):
        num = float(input(f"Enter number {i+1}: "))
        total_sum += num

#results
print(f"The sum of all numbers is: {total_sum}")