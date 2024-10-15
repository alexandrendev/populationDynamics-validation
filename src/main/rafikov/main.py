import sys

sys.path.append('/home/bolsistas/.alx/populationDynamics-validation/src/main')


from scipy.integrate import solve_ivp
import numpy as np
from time import time
from Data import *
import utils as u

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




days = (0, 10)
timeInterval = np.linspace(*days, 10)


res = solve_ivp(system, days, initialValues, t_eval=timeInterval)

results = []

for i in range(len(res.t)):
   u.saveFile(file, Data(res.t[i], res.y[0][i], res.y[1][i], res.y[2][i]))
   # results.append(Data(res.t[i], res.y[0][i], res.y[1][i], res.y[2][i]))
   # print(results)
# def hostVariation(r, hosts, K, n1) -> HostState:
#     return HostState.NATURAL_CASE_DEATH

