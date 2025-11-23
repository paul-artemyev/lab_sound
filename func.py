import numpy as np
import os
from const import *

def find_max_line_number(filename):
    max_value = -1
    max_line = -1
    
    with open(filename, 'r') as file:
        for line_num, line in enumerate(file, 1):  # начинаем с 1
            line = line.strip()
            if line:
                try:
                    num = int(line)
                    if num > max_value:
                        max_value = num
                        max_line = line_num
                except ValueError:
                    continue
    
    return max_line, max_value

def speedOfSound(difference):
    return length*nu/difference

def calculate_statistics(values):
    if not values:
        return None
    
    return {
        'mean': np.mean(values),
        'std': np.std(values)
    }

def process_folder(folder):
    file_0 = os.path.join(folder, 'data_0.txt')
    file_1 = os.path.join(folder, 'data_1.txt')

    if not os.path.exists(file_0) or not os.path.exists(file_1):
        print(f"Предупреждение: файлы в папке {folder} не найдены")
        return None
    
    line_0, max_0 = find_max_line_number(file_0)
    line_1, max_1 = find_max_line_number(file_1)
    
    difference = line_1 - line_0
    
    return {
        'max_0': max_0,
        'max_1': max_1,
        'difference': difference,
        'line_0': line_0,
        'line_1': line_1,
        'soundSpeed': speedOfSound(difference)
    }

def analyze_group(results, group_indices):
    group_speeds = [results[folder]['soundSpeed'] for folder in group_indices if folder in results]
    return calculate_statistics(group_speeds), group_speeds

def print_statistics(stats, group_name, values):
    print(f"\n{group_name}:")
    if stats:
        print(f"  Среднее: {stats['mean']:.4f}")
        print(f"  Разброс: {stats['std']:.4f}")
    else:
        print("  Нет данных")

def plot_co2(hum, co2Max):
    T = T0 + temp

    co2X = np.linspace(0, co2Max / 100, 100)
    h2oX = 0.01*hum*p/p0
    airX = 1 - h2oX - co2X

    Cp = airMu * airCp * airX + h2oMu * h2oCp * h2oX + co2Mu * co2Cp * co2X
    Cv = airMu * airCv * airX + h2oMu * h2oCv * h2oX + co2Mu * co2Cv * co2X

    gamma = Cp / Cv
    mu = airMu * airX + h2oMu * h2oX + co2Mu * co2X

    soundSpeed = np.sqrt(gamma * R * T / (mu / 1000))

    return co2X * 100, soundSpeed