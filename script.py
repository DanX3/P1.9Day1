import numpy as np
import matplotlib.pyplot as pl

xval = np.linspace(-5, 5, 100)
    

yval = xval**2 + 1

pl.plot(xval, yval)
pl.show()

