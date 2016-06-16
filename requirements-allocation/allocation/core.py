import random
from .population import Population


class Core(object):

    def __init__(self, requirements, analysts):
        self.analysts = analysts
        self.requirements = requirements
        self.population = Population(requirements, analysts)
        self.solution = None

    def run(self):
        sub_population = self.population.chromossomes
        sub_size = len(sub_population)

        for i in range(1000):
            best_solution = max(sub_population)
            if best_solution.fitness >= 8 * len(best_solution.genes):
                break

            for i in range(sub_size):
                parent1 = random.choice(sub_population)
                parent2 = random.choice(sub_population)
                sub_population.append(parent1.crossover(parent2))
                sub_population.append(parent2.crossover(parent1))

            # sub_population = self.select_survivors(sub_population, sub_size)

        self.solution = max(sub_population)

    def select_survivors(self, population, size):
        survivors = sorted(population, reverse=True)[:size]
        return survivors
