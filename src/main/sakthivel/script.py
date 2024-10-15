from scipy.integrate import solve_ivp
import numpy as np

r = 0.1
K = 25000
m1 = 0.15
beta = 4.147e-07
m2 = 0.036
n2 = 0.0625
gamma = 40
m3 = 0.5
def system(t, y) -> list(float):
    H, I, P = y
    
    dHdt =beta * (1 - H/K) * H - m1 * H - 
    dIdt = 
    dPdt =
    