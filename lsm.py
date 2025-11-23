import numpy as np
def lsm(x,y):
    n = len(x)
    x_mean=np.mean(x)
    y_mean=np.mean(y)
    x2=np.mean(x**2)
    y2=np.mean(y**2)
    xy=np.mean(x*y)
    D_xx = x2-x_mean**2 #дисперсия x
    D_yy = y2-y_mean**2 # дисперсия y
    D_xy = xy-x_mean*y_mean # ковариация x,y
    k = D_xy/D_xx
    b = y_mean-k*x_mean
    sigma_k_random = np.sqrt((D_yy/D_xx-k**2)/(n-1)) # случайная погрешность k
    sigma_b_random = sigma_k_random*np.sqrt(x2) # случайная погрешность b
    x = np.linspace(0, np.max(x), 20)
    y = k*x+b
    return k, sigma_k_random, b, sigma_b_random
