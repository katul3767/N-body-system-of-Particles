import rebound
import sys
import matplotlib.pyplot as plt
import numpy as np

sim = rebound.Simulation()
sim.integrator ="leapfrog"
sim.add(m= 1, x= 0.504457024898985, y= 1.058520304479640 , vx= -0.588406317185329, vy= -0.507208447977203)
sim.add(m= 1, x= 1.581323394863468, y= 1.639575414656912 , vx= 0.377133148141246, vy= 0.459577663854508)
sim.add(m= 1, x= -1.960902462113829, y= -1.605062781926992 , vx= -0.377133148141246, vy= -0.459577663854508)
sim.add(m= 1, x= -0.884036092149343, y= -1.024007671749708 , vx= 0.588406317185329, vy= 0.507208447976862)
sim.move_to_com()

sim.dt = sim.particles[1].P*1e-4
total_time = sim.particles[1].P*100
N = 1000
x = np.zeros((sim.N, N))
y = np.zeros_like(x)
times = np.linspace(0, 2*np.pi, N)
for i, t in enumerate(times):
    print(t, end="\r")
    sim.integrate(t, exact_finish_time=0)
    for j in range(sim.N):
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
fig.savefig("orbit.pdf")