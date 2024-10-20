from plot.Parameter import Parameter
import matplotlib.pyplot as plt

def plotGraph(time: Parameter, parameters: list[Parameter], imageName: str) -> None:
    plt.figure(figsize=(10, 6))
    
    for param in parameters:
        plt.plot(time.values, param.values, label=param.label, marker='.')
        

    plt.title('Dinamica Populacional ao Longo do Tempo')
    plt.xlabel('Tempo (dias)')
    plt.ylabel('Densidade Populacional')
    plt.legend()
    plt.grid()
    plt.savefig(f'graphs/{imageName}.png') 