
#Display numbers that appear multiple times.
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
    
# Count duplicates
count_dict = {}
for num in numbers:
    count_dict[num] = count_dict.get(num, 0) + 1
    
# Display duplicates
found_duplicates = False
print("\nNumbers appearing multiple times:")
for num in sorted(count_dict.keys()):
    if count_dict[num] > 1:
        print(f"{num} appears {count_dict[num]} times")
        found_duplicates = True
    
if not found_duplicates:
    print("(No duplicates found)")

