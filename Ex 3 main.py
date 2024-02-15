import rebound
import sys
import matplotlib.pyplot as plt
import numpy as np
import sympy

sim = rebound.Simulation()
sim.integrator ="leapfrog"

distance = 1.0
saturnmass = 2.85716656e-04

N = int(input("enter the value of N:"))
#N = 35
r = 1
gamma = float(input("enter value of gamma:"))
#gamma = 2.3753
m = (gamma*saturnmass)/(N**3)
#m = 1.325513229e-2
G = sim.G
def fun(N):
    a = 0
    for i in range(1,N):
        b = 4*np.sin(np.pi*i/N)
        a += 1/b
    return a
i = [0,N]
In = fun(N)
v = np.sqrt(G*saturnmass/r**3 + G*m*In/r**3)
#summation = 0
#for i in range(1, n + 1):
    #summation += i # shorthand for summation = summation + i 
dphi = 2*np.pi/(N)
phi = 0

sim.add(m = 2.85716656e-04)
for i in range (0,N):
    x = distance*np.cos(phi)
    y =  distance*np.sin(phi)
    vx = -v * np.sin(phi)
    vy = v * np.cos(phi)
    sim.add (m=m, x=x, y=y, vx=vx, vy=vy)
    phi += dphi
sim.move_to_com()
sim.dt = sim.particles[i].P*1e-4
total_time = sim.particles[i].P*100
period = 2*np.pi
Noutputs = 100
Norbits = 10
Nsteps = Norbits*Noutputs
times = np.linspace(0, Norbits*period, Nsteps)
x = np.zeros((N+1, Nsteps))
y = np.zeros((N+1, Nsteps))
#number of orbits, etcpp
for i, t in enumerate(times):
    print(t, end="\r")
    sim.integrate(t, exact_finish_time=0)
    for j in range(0, N):
        x[j, i] = sim.particles[j].x
        y[j, i] = sim.particles[j].y
print()
fig, ax = plt.subplots()
ax.scatter(x,y,s=1)
ax.set_title("Orbit with step size %g" % sim.dt)
ax.set_aspect("equal")
ax.set_xlabel("x coordinate")
ax.set_ylabel("y coordinate")
plt.grid("True")
fig.savefig("orbita0.pdf")