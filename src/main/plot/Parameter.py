import numpy as np
class Parameter:
    def __init__(self, label: str, values: np.ndarray):
        self.label = label
        self.values = values
        