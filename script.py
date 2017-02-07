import numpy as np
import matplotlib.pyplot as pl

xval = np.linspace(-3, 3, 100)
print "Usage:"
print "1 - y = x"
print "2 - y = sin(x)"
print "3 - y = cos(x)"
print "4 - y = tan(x)"
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

