class Data:
    def __init__(self, time, hosts, infected, parasitoids):
        self.time = time
        self.hosts = hosts
        self.infected = infected
        self.parasitoids = parasitoids
        
    def __str__(self) -> str:
        return f'{self.time} {self.hosts} {self.infected} {self.parasitoids}\n'