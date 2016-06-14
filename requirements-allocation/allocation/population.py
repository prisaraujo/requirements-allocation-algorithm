from .gene import Gene


class Population(object):

    def __init__(self, requirement, analysts):
        self.analysts = analysts
        self.requirement = requirement
        self.genes = self.generate_genes()

    def generate_genes(self):
        return [
            Gene(
                analyst=analyst,
                requirement=self.requirement
            ) for analyst in self.analysts
        ]
