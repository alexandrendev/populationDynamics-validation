import sys
sys.path.append('/home/bolsistas/.alx/populationDynamics-validation/src/main')
# sys.path.append('/home/alx/Projetos/populationDynamics-validation/src/main')
from scipy.integrate import solve_ivp
import numpy as np
from time import time
import utils as u
from plot.Parameter import Parameter
from plot.plot import *
from Param import *


def rafikov(parameters: Param, days: int, instantsPerDay: int)-> None:
   r = parameters.r
   K = parameters.K
   n1 = parameters.n1
   beta = parameters.beta
   m2 = parameters.m2
   n2 = parameters.n2
   gamma = parameters.gamma
   m3 = parameters.m3


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




   duration = (0, days)
   timeInterval = np.linspace(*duration, days*instantsPerDay)


   res = solve_ivp(system, duration, initialValues, t_eval=timeInterval)

   time_points = Parameter('Time(Days)', res.t)

   params = [
      Parameter('Hosts(H)', res.y[0]),
      Parameter('Infected(I)', res.y[1]),
      Parameter('Parasitoids(P)', res.y[2])
   ]

   plotGraph(time_points, params, f'rafikov-{parameters.equilibrium.description}')


param = Param(Equilibrium.FIRST)
rafikov(param, 1000, 10)

param = Param(Equilibrium.SECOND)
rafikov(param, 1000, 10)

param = Param(Equilibrium.THIRD)
rafikov(param, 1000, 10)