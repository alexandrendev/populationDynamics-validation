import sys
sys.path.append('/home/bolsistas/.alx/populationDynamics-validation/src/main')
# sys.path.append('/home/alx/Projetos/populationDynamics-validation/src/main')

from scipy.integrate import solve_ivp
import numpy as np
from plot.Parameter import Parameter
from plot.plot import *
from Param import *


def molnar(param: Param, days: int, instantsPerDay: int)-> None:

    r = param.r
    K = param.K
    m1 = param.m1
    m2 = param.m2
    m3 = param.m3
    m4 = param.m4
    n1 = param.n1
    n3 = param.n3
    alpha = param.alpha
    beta = param.beta
    gamma1 = param.gamma1
    gamma2 = param.gamma2
    
    
    def system(t, y) -> list[float]:
        x1, x2, x3, x4 = y
        
        dx1dt = r * x1 * (1 - x1 / K) - m1 * x1 - n1 * x1 - alpha * x1 * x2
        dx2dt = alpha * gamma1 * x1 * x2 - m2 * x2
        dx3dt =  n1 * x1 - m3 * x3 - n3 * x3 - beta * x3 * x4
        dx4dt = beta * gamma2 * x3 * x4 - m4 * x4
        
        return [dx1dt, dx2dt, dx3dt, dx4dt]
    
    
    
    x1 = 1000
    x2 = 7000
    x3 = 2500 
    x4 = 2000
    
    initialValues =[x1, x2, x3, x4]
    
    duration = (0, days)
    timeInterval = np.linspace(*duration, days*instantsPerDay)
    
    res = solve_ivp(system, duration, initialValues, t_eval=timeInterval)

    time_points = Parameter('Time(Days)', res.t)

    params = [
        Parameter('x1', res.y[0]),
        Parameter('x2', res.y[1]),
        Parameter('x3', res.y[2]),
        Parameter('x4', res.y[3])
    ]

    plotGraph(time_points, params, f'molnar-{param.equilibrium.description}')

parameters = Param(Equilibrium.FIRST)
molnar(parameters, 1000, 10)
