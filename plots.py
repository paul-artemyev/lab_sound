import matplotlib.pyplot as plt
import numpy as np
from func import plot_co2

def init(ax):
    # plt.rcParams.update({
    #     'text.usetex': True,
    #     'font.family': 'serif',
    #     'text.latex.preamble': r'\usepackage[utf8]{inputenc} \usepackage[russian]{babel}',
    # })    
    ax.set_xlabel('Концентрация CO_2, %')
    ax.set_ylabel('Скорость звука, м/с')
    ax.grid(which='major', linestyle='-')
    ax.minorticks_on() 
    ax.grid(which='minor', linestyle='--', linewidth=0.5)
    

def plot_sound_speed(ax,hum):
    x,y = plot_co2(hum, 5)
    ax.plot(x, y, linewidth=2, label=f'Влажность {hum}%', marker='o', ms=0)

def horizontal_exp_lines(ax,soundSpeed, hum):
    x = np.linspace(0, 5, 100)  # исправлено: от 0 до 5% CO2
    y = np.full(100, soundSpeed)  # массив одинаковых значений
    ax.plot(x, y, label=f'Измерение при влажности {hum} %)', linestyle='--', color='red', linewidth=1)
