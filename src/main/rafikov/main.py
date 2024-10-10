
from scipy.integrate import solve_ivp
import numpy as np


# For numerical simulations of interactions between the sugar-
# cane borer and its parasitoid we use the following values of model


# coefficients: n1 = 1/50, n2 = 1/16, g = 40, m2 = 0.036, m3 = 0.5,
# K = 25, 000.
# dP / dt = lambda * n2 * infected - m3 * parasitoid

r = 0.1
K = 25000
n1 = 0.15
beta = 4.147e-07
m2 = 0.036
n2 = 0.0625
gamma = 40
m3 = 0.5


def sistema(t, y) ->  list[float]:
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


res = solve_ivp(sistema, days, initialValues, t_eval=timeInterval)


for i in range(len(res.t)):
   print(f'Tempo: {res.t[i]:.2f} -> Hosts: {res.y[0][i]:.2f}, Infected: {res.y[1][i]:.2f}, Parasitoid: {res.y[2][i]:.2f}')
# def hostVariation(r, hosts, K, n1) -> HostState:
  
  
  
#     return HostState.NATURAL_CASE_DEATH

