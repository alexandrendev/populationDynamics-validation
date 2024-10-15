# populationDynamics-validation

# Main

- [ ] Implementar algoritmo usando Monte Carlo reproduzindo dados do artigo
--------
### Rafikov

- [x] Ler artigo [Rafkov](file:///home/bolsistas/Downloads/2014_DynamicalBehavior_Rafkov.pdf)
- [x] Implementar algoritmo reproduzindo os dados do artigo

### Sakthivel

- [ ] Ler artigo [Rafkov](file:///home/bolsistas/Downloads/2017_NonfragileControl_Sakthivel.pdf)
- [ ] Implementar algoritmo reproduzindo os dados do artigo 

$$
\begin{cases}
\frac{dE}{dt} = \beta\left(1 - \frac{E}{K}\right) E - m_1 E - n_1 x_1 - \alpha E I \\
\frac{dI}{dt} = \alpha E I - m_2 I - n_2 I + U \\
\frac{dP}{dt} = n_1 E - m_3 P - n_3 P
\end{cases}
$$
- **E:** Eggs Density (Densidade de ovos)
- **P:** Parasitised Eggs (Ovos Infectados)
- **H:** Larvae Density Population (População de larvas)