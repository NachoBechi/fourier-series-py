import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

# Generate the coeficients: a_0, a_n, b_n of fourier series of f
def coeficientes_fourier(f, N):
    """
    Given a continuous function f on [-π, π], the function returns the value a_0 and
    the lists a_n and b_n with the first N coefficients of the Fourier series
    """

    # Limits and length of the interval where f is studied
    li,lf = -np.pi,np.pi
    L = np.pi

    # Constant term
    a_0 = 1/L * integrate.quad(lambda x: f(x),li, lf)[0]

    # Inicialize the list of sen and cos coeficients
    a_n = np.zeros(N)
    b_n = np.zeros(N)

    # We calculate each term using numerical integration
    for i in range(1,N+1):
        a_n[i-1]=1/L*integrate.quad(lambda x: f(x)*np.cos(i*np.pi*x/L), li, lf)[0]
        b_n[i-1]=1/L* integrate.quad(lambda x: f(x)*np.sin(i*np.pi*x/L), li, lf)[0]

    return a_0/2.0, a_n, b_n

# Define a function
def f(x):
    return -x**2

# Define N
N = 10

# Define coeficients
a_0, a_n, b_n = coeficientes_fourier(f,N)

x_arange = np.arange(-np.pi, np.pi, .01)
print(x_arange)
y = []

for m in x_arange:
    sum = a_0
    k = 0

    x = m
    while k < N:
        i = a_n[k]
        j = b_n[k]
        
        sum += i*np.cos((k+1)*x)
        sum += j*np.sin((k+1)*x)
        k +=1
    y.append(sum)

plt.axis([-np.pi*2, np.pi*2, -np.pi*2, np.pi*3])
plt.plot(x_arange, y)
plt.show()
