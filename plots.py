import matplotlib.pyplot as plt
import numpy as np
from func import plot_co2

def init(ax):
    ax.set_xlabel('Концентрация CO₂, %')
    ax.set_ylabel('Скорость звука, м/с')
    ax.grid(which='major', linestyle='-')
    ax.minorticks_on() 
    ax.grid(which='minor', linestyle='--', linewidth=0.5)
    ax.set_xlim([0, 6])
    ax.set_ylim([338,347])
    

def plot_sound_speed(ax,hum, color):
    x,y = plot_co2(hum, 6)
    ax.plot(x, y, linewidth=2, label=f'Влажность {hum}%', marker='o', ms=0, color = color)

def horizontal_exp_lines(ax,soundSpeed, hum, x0, color):
    x = np.linspace(-1, x0+0.5, 100)
    y = np.full(100, soundSpeed)
    ax.plot(x, y, label=f'Скорость звука: {soundSpeed:.1f} м/с', linestyle=':', linewidth=2, color = color)

def vertical_exp_line(ax, x_coord, hum, y0, color):
    y = np.linspace(338, y0+0.01, 100)
    x = np.full(100, x_coord)
    ax.plot(x, y, label=f'CO₂: {x_coord:.2f}% ({hum}% влаж.)', linestyle=':', linewidth=2, color = color)