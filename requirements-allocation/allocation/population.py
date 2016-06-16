from .chromossome import Chromossome


class Population(object):

    def __init__(self, requirements, analysts):
        self.analysts = analysts
        self.requirements = requirements
        self.chromossomes = self.generate_population()

    def generate_population(self):
        return [
            Chromossome(requirements=self.requirements, analysts=self.analysts)
            for i in range(50)
        ]
