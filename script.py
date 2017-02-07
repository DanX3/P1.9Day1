import numpy as np
import matplotlib.pyplot as pl

xval = np.linspace(-5, 5, 100)
print "Usage:"
print "1 - y = x"
choice = input();

if choice == 1:
    f = lambda x: x

yval = f(xval)

pl.plot(xval, f(xval))
pl.show()

