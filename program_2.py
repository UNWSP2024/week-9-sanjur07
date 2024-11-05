# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).

import random

def write_random_numbers(filename, count):
    if count > 1000:
        print("The maximum number of random numbers allowed is 1000.")
        return
    try:
        with open(filename, 'w') as file:
            for _ in range(count):
                
                number = random.randint(1, 500)
                
                file.write(f"{number}\n")
        print(f"{count} random numbers have been written to {filename}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    try:
        
        count = int(input("Enter the number of random numbers to generate (up to 1000): "))
        write_random_numbers("random_numbers.txt", count)
    except ValueError:
        print("Please enter a valid integer.")
