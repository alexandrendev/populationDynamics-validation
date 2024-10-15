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
- **n1:** fração de ovos que eclodiram no tempo t
- **n2:** fração de ovos parasitados em que o parasita adulto emerge no tempo t
- **n3:** fração da população de larvas que viraram pulpa no tempo t
- **k:** Limite de carga/capacidade
- **beta:** taxa de reprodução
- **m1:** Taxa de mortalidade do ovo
- **m2:** Taxa de mortalidade dos ovos infectados
- **m3:** Taxa de mortalidade das larvas
- *U:* 
