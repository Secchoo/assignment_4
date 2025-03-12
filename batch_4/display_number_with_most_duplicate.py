#Find the number with most duplicates.
count_dict = {}
    
print("Enter numbers (invalid input to stop):")
while True:
    try:
        num = int(input("Number: "))
        count_dict[num] = count_dict.get(num, 0) + 1
    except ValueError:
        break
    
if not count_dict:
    print("\nNo valid numbers entered.")
    exit()
    
# Find maximum frequency
max_freq = max(count_dict.values())
most_frequent_nums = [num for num, freq in count_dict.items() if freq == max_freq]
    
print("\nNumber(s) appearing most frequently:")
for num in sorted(most_frequent_nums):
    print(f"{num} appears {max_freq} times")