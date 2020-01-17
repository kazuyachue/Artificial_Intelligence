import math
import matplotlib.pyplot as plt

dt = 0.01
total_time = 20
N = 2000  #total_time / dt

def constantf():   #returns f(t) for constant force
    def f(t):
        return 0.5
    return f

def harmonicf(omega): #returns f(t) for harmonic driver
    def f(t):
        return 5.0 * math.sin(omega * t)
    return f

def pulsef(t0, lambda_value): #returns f(t) for pulse driver
    def f(t):
        return 5.0 * math.exp(-1.0 * lambda_value * (t-t0) * (t-t0))
    return f

def leap_frog(dt, N, f, omega, beta): #f is a function
    def F(t,x,v):
        return f(t) - omega * omega * x - beta * v

    t = [0.0] * N  #initializing lists
    x = [0.0] * N
    v = [0.0] * N

    ti = dt / 2.0  #intermediate variables
    xi = 0.0
    vi = F(0,0,0) * dt / 2.0

    for i in range(0, N-1):  #main loop
        t[i+1] = t[i] + dt
        x[i+1] = x[i] + vi * dt
        v[i+1] = v[i] + F(ti, xi, vi) * dt
        ti = ti + dt
        xi = 0.5 * (x[i+1] + x[i]) + v[i+1] * dt
        vi = 0.5 * (v[i+1] + v[i]) + F(t[i+1], x[i+1], v[i+1]) * dt

    return t,x,v

#Constant Force and Weak Damping
t,x,v = leap_frog(dt, N, constantf(), 0.5, 0.1)
plt.plot(t, x)
plt.title('Solution of Reduced System with Constant Force and Weak Damping')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.show()

#Constant Force and Critical Damping
t,x,v = leap_frog(dt, N, constantf(), 0.5, 1)
plt.plot(t, x)
plt.title('Solution of Reduced System with Constant Force and Critical Damping')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.show()

#Constant Force and Strong Damping
t,x,v = leap_frog(dt, N, constantf(), 0.5, 5)
plt.plot(t, x)
plt.title('Solution of Reduced System with Constant Force and Strong Damping')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.show()


#Harmonic Driver and Weak Damping
t,x,v = leap_frog(dt, N, harmonicf(0.5), 0.5, 0.1)
plt.plot(t, v)
plt.title('Solution of Reduced System with Harmonic Driver and Weak Damping')
plt.xlabel('t')
plt.ylabel('v(t)')
plt.show()

#Harmonic Driver and Critical Damping
t,x,v = leap_frog(dt, N, harmonicf(0.5), 0.5, 1)
plt.plot(t, v)
plt.title('Solution of Reduced System with Harmonic Driver and Critical Damping')
plt.xlabel('t')
plt.ylabel('v(t)')
plt.show()

#Harmonic Driver and Strong Damping
t,x,v = leap_frog(dt, N, harmonicf(0.5), 0.5, 5)
plt.plot(t, v)
plt.title('Solution of Reduced System with Harmonic Driver and Strong Damping')
plt.xlabel('t')
plt.ylabel('v(t)')
plt.show()


#Pulse Driver and Weak Damping
t,x,v = leap_frog(dt, N, pulsef(5, 0.25), 0.5, 0.1)
plt.plot(x, v)
plt.title('Solution of Reduced System with Pulse Driver and Weak Damping')
plt.xlabel('x(t)')
plt.ylabel('v(t)')
plt.show()

#Pulse Driver and Critical Damping
t,x,v = leap_frog(dt, N, pulsef(5, 0.25), 0.5, 1)
plt.plot(x, v)
plt.title('Solution of Reduced System with Pulse Driver and Critical Damping')
plt.xlabel('x(t)')
plt.ylabel('v(t)')
plt.show()

#Pulse Driver and Strong Damping
t,x,v = leap_frog(dt, N, pulsef(5, 0.25), 0.5, 5)
plt.plot(x, v)
plt.title('Solution of Reduced System with Pulse Driver and Strong Damping')
plt.xlabel('x(t)')
plt.ylabel('v(t)')
plt.show()
