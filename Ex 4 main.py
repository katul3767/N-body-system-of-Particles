#!/usr/bin/env python3
import rebound
import numpy as np
import matplotlib.pyplot as plt

solarmass = 1.989e30
au = 1.496e11
gravitationalconstant = 6.67408e-11
year_in_seconds = 365.25*24*3600

sim = rebound.Simulation()
N = 10003
sim.units = ("kg", "m", "s")
sim.add(m=1.989e30)
sim.add(m = 6.39e23, a = 1.5 * au, e = 0.0934)
sim.add(m = 1.898e27, a = 5.2 * au, e = 0.048)

N_testparticle = 10000
a_ini = np.linspace(2*au, 4*au, N_testparticle)
for a in a_ini:
    sim.add(a=a, f=np.random.rand()*2.*np.pi, e=0.5*np.random.rand())
orbit = 2*np.pi*np.sqrt(8*au*au*au/(gravitationalconstant*solarmass))
print("Orbit in years %g" % (orbit/year_in_seconds))
sim.dt = orbit*1e-2
sim.N_active = 3
sim.integrator = "leapfrog"
N_out = 100
xy= np.zeros((N_testparticle,2))
a_ecc = np.zeros((N_testparticle, 2))
#a = [a1, a2, a3, a4, a10 ]
#a[] = np.zeros()
#%store
#times = np.linspace(0, orbit, N_out)
simulation_time = 1e6 * year_in_seconds
times = np.linspace(0, simulation_time, N_out)
sim.move_to_com()
for i, time in enumerate(times):
    print("%.2g percent done" % (time/simulation_time*100))
    sim.integrate(time)
    for j, p in enumerate(sim.particles[3:]):
        xy[j] = [p.x, p.y]
        a_ecc[j] = [p.a, p.e]
    fig, ax = plt.subplots()
    # ax.scatter(a_ecc[:,0]/au,a_ecc[:,1], s=1)
    ax.set_xlabel("semi-major axis")
    ax.set_ylabel("number of asteroids in bin")
    ax.set_xlim(2,4)
# these lines kill the computer
#    bins = np.arange(0, 10000, 0.0005)
#    plt.hist(a_ecc[:,:,0]/au, bins =bins)
# you're giving a numpy array as argument for bins, which does
# not do what you want, see https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.hist.html
    sma = a_ecc[:,0]
    sma /= au
    dbin = 0.05
    bins = int((4-2)/0.005)
    ax.hist(sma, bins=bins, range=(2,4))
    ax.set_title('dbin = 0.005 au')
    fig.savefig("kirk" + str(i) + ".pdf")
    plt.close(fig)
    #plt.show()


sim.save("kirkwood_gaps.rebound")
