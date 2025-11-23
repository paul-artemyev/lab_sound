import matplotlib.pyplot as plt
import numpy as np
from func import plot_co2

def init(ax):
    # plt.rcParams.update({
    #     'text.usetex': True,
    #     'font.family': 'serif',
    #     'text.latex.preamble': r'\usepackage[utf8]{inputenc} \usepackage[russian]{babel}',
    # })    
    ax.set_xlabel('Концентрация CO₂, %')
    ax.set_ylabel('Скорость звука, м/с')
    ax.grid(which='major', linestyle='-')
    ax.minorticks_on() 
    ax.grid(which='minor', linestyle='--', linewidth=0.5)
    

def plot_sound_speed(ax,hum):
    x,y = plot_co2(hum, 6)
    ax.plot(x, y, linewidth=2, label=f'Влажность {hum}%', marker='o', ms=0)

def horizontal_exp_lines(ax,soundSpeed, hum, x0):
    x = np.linspace(x0-0.5, x0+0.5, 100)
    y = np.full(100, soundSpeed)
    ax.plot(x, y, label=f'Измерение при влажности {hum} %)', linestyle=':', linewidth=2, color = 'red')

def vertical_exp_line(ax, x_coord, hum, y0):
    y = np.linspace(y0*0.995, y0*1.005, 100)
    x = np.full(100, x_coord)
    ax.plot(x, y, label=f'CO₂: {x_coord:.2f}% ({hum}% влаж.)', linestyle=':', linewidth=2, color = 'red')