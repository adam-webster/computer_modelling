import math as m
import cmath as cm
import matplotlib.pyplot as plt


N = 10


#prepare data lists for plot


def main() :
    x_values = []
    y_values = []
    x = 0 
    for i in range(N) :
        fourier = m.sin((2*i - 1) * x) / (2*i - 1)
        x += fourier
    return fourier
    x_values.append(x)
    y_values.append(fourier)


'''
for i in range(N):
    x_0 = 
    i = 1
    x = 2 * m.pi / i
    y = harmonic_function(i, x)
    x_values.append(x)
    y_values.append(y)
    i += 1
'''

      
main()

plt.plot(x_values, y_values)
plt.show()

