import numpy as np
import matplotlib.pyplot as pl

xval = np.linspace(-5, 5, 100)
choice = input();

if choice == 1:
    f = lambda x: x
if choice == 2:
    f = lambda x: np.sin(x)
if choice == 3:
    f = lambda x: np.cos(x)
if choice == 4:
    f = lambda x: np.tan(x)

yval = f(xval)

pl.plot(xval, f(xval))
pl.show()

