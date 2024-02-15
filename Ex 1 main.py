import rebound
import sys
import matplotlib.pyplot as plt
import numpy as np

sim = rebound.Simulation()
sim.integrator ="WHFAST"
sim.dt = 1e-4
sim.add(m=1.0)
sim.add(m=1e-3, a=1.0, e=0.3)
sim.move_to_com()
Norbits = 1
Nsteps = Norbits*1000
times = np.linspace(0, Norbits*2*np.pi, Nsteps)
x = np.zeros((sim.N, Nsteps))
y = np.zeros_like(x)
energy = np.zeros(Nsteps)
for i, t in enumerate(times):
    print(t, end="/r")
    sim.integrate(t, exact_finish_time=0)
    energy[i] = sim.calculate_energy()
    for j in range(sim.N):
        x [j, i] = sim.particles[j].x
        y [j, i] = sim.particles[j].y

#fig, ax = plt.subplots()
#ax.scatter(x,y,s=2)
#ax.set_title("Orbit with step size %g" % sim.dt)
#ax.set_aspect("equal")
#ax.set_xlabel("x coordinate")
#ax.set_ylabel("y coordinate")
#plt.grid("True")
#fig.savefig("orbitWHFAST"+str(sim.dt)+".pdf")

#fig, ax = plt.subplots()
#ax.scatter(times, np.abs(energy-energy[0])/np.abs(energy[0]), s=2)
#print(energy)
#ax.set_title("Energy with step size %g" % sim.dt)
#ax.set_xlabel("time")
#ax.set_yscale("log")
#ax.set_ylabel("energy")
#plt.grid("True")
#fig.savefig("energyWHFAST"+str(sim.dt)+".pdf")
#print("Done.")

L = np.zeros((3, Nsteps))
Lz = np.zeros((1, Nsteps))
for i, t in  enumerate(times):
    L[:,i] = sim.calculate_angular_momentum()
    Lz[:,i] = L[:,i][2]
    print(L[:,i])

fig, ax = plt.subplots()
ax.scatter(times, np.abs(L[2]-L[2][0])/np.abs(L[2][0]), s=2)
#print(Relative error of Angular Monentum)
ax.set_title("Relative error of Angular Monentum with step size %g" % sim.dt)
ax.set_xlabel("times")
#ax.set_yscale("log")
ax.set_ylabel("Relative error of Angular Monentum")
plt.grid("True")
fig.savefig("Relative error of Angular Monentum WHFAST"+str(sim.dt)+".pdf")
print("Done.")
