from enum import Enum

class Equilibrium(Enum):
    FIRST = (1, 'First-Equilibrium')
    SECOND = (2, 'Second-Equilibrium')
    THIRD = (3, 'Third-Equilibrium')
    
    def __init__(self, value, description):
        self._value_ = value
        self.description = description

class Param:
    def __init__(self, equilibrium: Equilibrium):
        self.r = 0.19
        self.K = 25000
        self.m1 = 0.03566
        self.m2 = 0.03566
        self.m3 = 0.00256
        self.m4 = 1
        self.n1 = 0.1
        self.n3 = 0.02439
        self.alpha = 0.0000075
        self.beta = 0.0000083
        self.gamma1 = 2.29
        self.gamma2 = 40
        self.equilibrium = equilibrium