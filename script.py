import numpy as np
import matplotlib.pyplot as pl

xval = np.linspace(-5, 5, 100)
choice = input();

if choice == 1:
    f = lambda x: x
if choice == 2:
    f = lambda x: x**2 + 1

yval = f(xval)

pl.plot(xval, f(xval))
pl.show()

