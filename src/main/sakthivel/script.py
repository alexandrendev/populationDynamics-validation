from scipy.integrate import solve_ivp
import numpy as np
import matplotlib as plt


m1 = 0.03566
m2 = 0.03566
m3 = 0.00256

n1 = 0.1
n2 = 0.10000
n3 = 0.02439
K = 25000

beta = 0.139
alpha = 0.0001723

def system(t, y) -> list[float]:
    E, P, L = y
    
    dEdt = beta * (1 - E/K) * E - m1*E - n1*E - alpha*E*P
    dPdt = alpha*E*P - m2*P - n2*P + U
    dPdt = n1*E - m2*L - n3*L
    
    return [dEdt, dPdt, dPdt]

EggsDensity = 800
ParasitisedEggs = 60
LarvaeDensity = 2500

initialValues = [ EggsDensity, ParasitisedEggs, LarvaeDensity]

days = (0, 10)
timeInterval = np.linspace(*days, 10)

res = solve_ivp(system, days, initialValues, t_eval=timeInterval)


# Resultados
time_points = res.t
E_values = res.y[0]  # Densidade de Ovos
P_values = res.y[1]  # Densidade de Ovos Parasitados
L_values = res.y[2]  # Densidade de Larvas

# Plotando os resultados
plt.figure(figsize=(10, 6))
plt.plot(time_points, E_values, label='Densidade de Ovos (E)')
plt.plot(time_points, P_values, label='Densidade de Ovos Parasitados (P)')
plt.plot(time_points, L_values, label='Densidade de Larvas (L)')
plt.title('Dinamica Populacional')
plt.xlabel('Tempo (dias)')
plt.ylabel('Densidade')
plt.legend()
plt.grid()
plt.show()
