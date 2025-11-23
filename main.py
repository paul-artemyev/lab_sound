import os
from func import *
from plots import *

folders = ['1', '2', '3', '4', 'co2-1','co2-2','co2-3','co2-4', 'co2-5', 'co2-6']
results = {}

for folder in folders:
    result = process_folder(folder)
    if result:
        results[folder] = result
    else:
         print(f"Предупреждение: файлы в папке {folder} не найдены")

first_group = folders[:4]
second_group = folders[4:]

stats1, speeds1= analyze_group(results, first_group)
stats2, speeds2= analyze_group(results, second_group)

print_statistics(stats1, "Первые 4 папки (1-4)", speeds1)
print_statistics(stats2, "Последние 6 папок (co2-1 - co2-6)", speeds2)

fig, ax = plt.subplots(figsize=(10, 6))
init(ax)
plot_sound_speed(ax,humidity)
plot_sound_speed(ax,humidity2)
horizontal_exp_lines(ax, stats1['mean'], humidity)
horizontal_exp_lines(ax, stats2['mean'], humidity2)

plt.legend()
plt.show()