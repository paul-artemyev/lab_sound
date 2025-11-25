with open('numbers.txt', 'w') as file:
    for i in range(1, 5000):
        file.write(str(i) + '\n')

print("Файл создан! Числа от 1 до 4999 записаны в столбик.")