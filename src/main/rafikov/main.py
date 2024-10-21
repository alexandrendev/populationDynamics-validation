import sys
# sys.path.append('/home/bolsistas/.alx/populationDynamics-validation/src/main')
sys.path.append('/home/alx/Projetos/populationDynamics-validation/src/main')
from scipy.integrate import solve_ivp
import numpy as np
from time import time
import utils as u
from plot.Parameter import Parameter
from plot.plot import *

file = f'files/rafikov/{time()}'

r = 0.1
K = 25000
n1 = 0.15
beta = 4.147e-07
m2 = 0.036
n2 = 0.0625
gamma = 40
m3 = 0.5


def system(t, y) ->  list[float]:
   H, I, P = y
  
   dHdt = r * (1 - H / K) * H - n1 * H - beta * H * P
   dIdt = beta * H * P - m2 * I - n2 * I
   dPdt = gamma * n2 * I - m3 * P
  
   return [dHdt, dIdt, dPdt]

  
Hosts = 3000
Infected = 600
Parasitoid = 3000

initialValues = [Hosts, Infected, Parasitoid]




days = (0, 1000)
timeInterval = np.linspace(*days, 10000)


res = solve_ivp(system, days, initialValues, t_eval=timeInterval)

time_points = Parameter('Time(Days)', res.t)

params = [
   Parameter('Hosts(H)', res.y[0]),
   Parameter('Infected(I)', res.y[1]),
   Parameter('Parasitoids(P)', res.y[2])
]

plotGraph(time_points, params, 'rafikov')

