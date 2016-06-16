import random
from .gene import Gene


class Chromossome(object):

    def __init__(self, requirements, analysts, genes=None):
        self.requirements = requirements
        self.analysts = analysts
        self.genes = genes if genes else self.build_genes()

    def __eq__(self, chromossome):
        return self.fitness == chromossome.fitness

    def __lt__(self, chromossome):
        return self.fitness < chromossome.fitness

    def __gt__(self, chromossome):
        return self.fitness > chromossome.fitness

    def build_genes(self):
        return [
            Gene(
                analyst=random.choice(self.analysts),
                requirement=requirement
            ) for requirement in self.requirements
        ]

    @property
    def fitness(self):
        return sum([gene.fitness for gene in self.genes])

    @property
    def survive_chance(self):
        return (self.fitness / len(self.genes)) * 10

    def crossover(self, chromossome):
        parent1_genes = self.genes[:int(len(self.genes)/2)]
        reqs = [gene.requirement for gene in parent1_genes]
        parent2_genes = [
            gene for gene in chromossome.genes if gene.requirement not in reqs
        ]
        genes = parent1_genes + parent2_genes

        new_chromossome = Chromossome(self.requirements, self.analysts, genes)
        if random.randint(0, 100) >= 75:
            new_chromossome.mutate()
        return new_chromossome

    def mutate(self):
        gene = random.choice(self.genes)
        gene.analyst = random.choice(self.analysts)
