import random
from .population import Population


class Core(object):

    def __init__(self, algorithm, requirements, analysts):
        self.analysts = analysts
        self.requirements = requirements
        self.selected_genes = []
        self.algorithm = algorithm(requirements, analysts)

    def run(self):
        for requirement in sorted(self.requirements, reverse=True):
            analysts = [
                analyst for analyst in self.analysts
                if analyst.pk != requirement.analyst
            ]
            population = Population(
                requirement=requirement,
                analysts=analysts
            )

            selected = self.algorithm.select_gene(population)
            selected.analyst.requirements_to_review.append(
                selected.requirement
            )
            self.selected_genes.append(selected)
