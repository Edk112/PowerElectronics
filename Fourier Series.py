import pylab
import numpy
import math

x = numpy.linspace(-10000,10000,10000) # 100 linearly spaced numbers
y = 1/(numpy.sqrt(1+4*numpy.pi*numpy.pi*x*x*10**-6)) # computing the values of sin(x)/x

# compose plot
pylab.plot(x,y) # sin(x)/x

 # same function with cyan dots
pylab.show() # show the plot
