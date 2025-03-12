#variable of total odds
odd_count = 0

#loop to get 10 numbers
for i in range(10):
        num = int(input(f"Enter number {i+1}: "))
    #counts odd numbers
        if num % 2 != 0:
            odd_count += 1

#results    
print(f"Number of odd numbers: {odd_count}")