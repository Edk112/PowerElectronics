import numpy as np
import matplotlib.pyplot as plt

def H(f):
    s = 1j*2*np.pi*f
    den = np.polyval([1,1],s*C*R)
    H = 1/den
    return H

R = 5*1e2
C = 10e-6

f_0 = 50.0
t = np.linspace(-50e-3, 50e-3, 5e2)
xt = np.cos(2*np.pi*f_0*t)
yt = abs(H(f_0))*np.cos(2*np.pi*f_0*t+np.angle(H(f_0)))

plt.subplot(2,1,1)
plt.plot(t, xt)
plt.title('sin')
plt.ylabel('$x(t)$')
plt.grid()

plt.subplot(2,1,2)
plt.plot(t,yt)
plt.xlabel('t(ms)')
plt.ylabel('$y(t)')
plt.grid()

plt.show()

