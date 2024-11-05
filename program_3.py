# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.
def sum_numbers_from_file():
    try:
        total = 0
        with open('numbers.txt', 'r') as file:
            for line in file:
                try:
                    # Convert each line to an integer and add it to the total
                    number = int(line.strip())
                    total += number
                except ValueError:
                    # Handle the case where a line cannot be converted to an integer
                    print(f"Warning: Could not convert '{line.strip()}' to an integer.")
        print(f"The total of the numbers in the file is: {total}")
    except IOError:
        print("An error occurred while trying to read the file 'numbers.txt'.")

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()