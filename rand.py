import random

def generate_numbers_file(filename, num_lines=5000, max_value=10000):
    with open(filename, 'w') as file:
        for i in range(num_lines):
            number = random.randint(0, max_value)
            file.write(f"{number}\n")

# Generate the file
generate_numbers_file('text.txt')
print("File 'numbers.txt' generated with 5000 random numbers!")