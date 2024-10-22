import sys
sys.path.append('/home/bolsistas/.alx/populationDynamics-validation/src/main')
# sys.path.append('/home/alx/Projetos/populationDynamics-validation/src/main')

from scipy.integrate import solve_ivp
import numpy as np
from plot.Parameter import Parameter
from plot.plot import *
from Param import *

def sakthivel(param: Param, days: int, instantsPerDay: int)-> None:
    m1 = param.m1
    m2 = param.m2
    m3 = param.m3
    n1 = param.n1
    n2 = param.n2
    n3 = param.n3
    K = param.K
    beta = param.beta
    alpha = param.alpha

    def system(t, y) -> list[float]:
        E, P, L = y

        dEdt = beta * (1 - E/K) * E - m1*E - n1*E - alpha*E*P
        dPdt = alpha*E*P - m2*P - n2*P
        dLdt = n1*E - m3*L - n3*L
        
        return [dEdt, dPdt, dLdt]
    

    EggsDensity = 800
    ParasitisedEggs = 100
    LarvaeDensity = 2500

    initialValues = [ EggsDensity, ParasitisedEggs, LarvaeDensity]

    duration = (0, days)
    timeInterval = np.linspace(*duration, days*instantsPerDay)

    res = solve_ivp(system, duration, initialValues, t_eval=timeInterval)

    timePoints = Parameter('Time(days)', res.t)
    params = [
        Parameter('Eggs Density(E)', res.y[0]),
        Parameter('Parasitized Eggs(P)', res.y[1]),
        Parameter('Larvae Density(L)', res.y[2])
    ]

    plotGraph(timePoints, params, f'sakthivel-{param.equilibrium.description}')

# parameters = Param(Equilibrium.FIRST)
# sakthivel(parameters, 2500, 10)

# parameters = Param(Equilibrium.SECOND)
# sakthivel(parameters, 2500, 10)

parameters = Param(Equilibrium.THIRD)
sakthivel(parameters, 2500, 10)

