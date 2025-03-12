
#insert 1st number
first_num = int(input("Enter first number: "))


total = first_num

#insert remaining numbers
for i in range(9):
        num = int(input(f"Enter number {i+2}: "))
        total -= num
    
print(f"The result is: {total}")