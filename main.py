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
print_statistics(stats1, "Атмосферный воздух", speeds1)
print_statistics(stats2, "Воздух из легких", speeds2)

print("--------------------------------")

k1,dk1,b1,db1 = coefs(humidity)
k2,dk2,b2,db2 = coefs(humidity2)
print(f"Влажность {humidity}% \n    Угловой коэффициент равен ({k1:.3f} ± {dk1:.3f})*10^2 м/с \n    Свободный член равен ({b1:.3f} ± {db1:.3f}) м/с \n")
print(f"Влажность {humidity2}% \n    Угловой коэффициент равен ({k2:.3f} ± {dk2:.3f})*10^2 м/с \n    Свободный член равен ({b2:.3f} ± {db2:.3f}) м/с \n")

print("--------------------------------")
x_intersect1, dx_intersect1 = find_intersection(k1,b1,stats1['mean'],dk1,db1, stats1['std'])
x_intersect2, dx_intersect2 = find_intersection(k2,b2,stats2['mean'],dk2,db2, stats2['std'])
print(f"Концентрация CO_2 при {humidity}: ({x_intersect1:.1f} ± {dx_intersect1:.1f}) %")
print(f"Концентрация CO_2 при {humidity2}: ({x_intersect2:.1f} ± {dx_intersect2:.1f}) %")

fig, ax = plt.subplots(figsize=(12, 8))
init(ax)
plot_sound_speed(ax,humidity, '#ff7f0e')
plot_sound_speed(ax,humidity2, '#9467bd')
horizontal_exp_lines(ax, stats1['mean'], humidity, x_intersect1, 'crimson')
horizontal_exp_lines(ax, stats2['mean'], humidity2, x_intersect2, 'royalblue')
vertical_exp_line(ax, x_intersect1, humidity, stats1['mean'], 'crimson')
vertical_exp_line(ax, x_intersect2, humidity2, stats2['mean'], 'royalblue')

plt.legend()
fig.savefig('plot.png', dpi = 300)
plt.show()