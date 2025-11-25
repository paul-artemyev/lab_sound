import matplotlib.pyplot as plt
import numpy as np

x_data = np.loadtxt('numbers.txt')*2
y1_data = np.loadtxt('co2-6/data_0.txt')
y2_data = np.loadtxt('co2-6/data_1.txt')

plt.figure(figsize=(10, 6))
plt.plot(x_data, y1_data, 'b-',label='Синяя линия: первый датчик', color='blue', linewidth=2)
plt.plot(x_data, y2_data, 'b-',label='Красная линия: второй датчик', color='red', linewidth=2)
plt.xlabel('t, микросекунды')
plt.ylabel('y, громкость')
plt.title('Зависимость громкости звука от времени')
plt.legend(fontsize=11, loc='upper right', framealpha=0.9)
plt.grid(True)
plt.show()