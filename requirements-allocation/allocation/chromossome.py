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

    def get_workload_by_analyst(self):
        workload = {}
        for gene in self.genes:
            if gene.analyst in workload:
                workload[gene.analyst] += gene.requirement.work_time
            else:
                workload[gene.analyst] = gene.requirement.work_time
        return workload

    @property
    def is_over_workload(self):
        workload_by_analyst = self.get_workload_by_analyst()
        for analyst in self.analysts:
            if analyst in workload_by_analyst:
                if workload_by_analyst[analyst] > analyst.speed_workload:
                    return True
        return False

    @property
    def is_invalid(self):
        if True in [gene.is_invalid for gene in self.genes]:
            return True

        if self.is_over_workload:
            return True

        return False

    @property
    def fitness(self):
        return sum([gene.fitness for gene in self.genes])

    @property
    def survive_chance(self):
        if self.fitness == 0:
            return 0
        return (self.fitness / len(self.genes)) * 10

    def crossover(self, chromossome):
        cutoff = random.randint(0, len(self.genes) - 1)
        parent1_genes = self.genes[:cutoff]
        reqs = [gene.requirement for gene in parent1_genes]
        parent2_genes = [
            gene for gene in chromossome.genes if gene.requirement not in reqs
        ]
        genes = parent1_genes + parent2_genes

        new_chromossome = Chromossome(self.requirements, self.analysts, genes)
        if random.randint(0, 100) <= len(genes):
            new_chromossome.mutate()
        return new_chromossome

    def mutate(self):
        gene = random.choice(self.genes)
        gene.analyst = random.choice(self.analysts)
