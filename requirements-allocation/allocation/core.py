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

        best_solutions = []

        for i in range(1000):
            print('iteration {}'.format(i+1))
            best_solution = max(sub_population)

            best_solutions.append(best_solution)
            if best_solution.fitness >= 8 * len(best_solution.genes):
                break

            children = []
            for parent1 in sub_population:
                parent2 = random.choice(sub_population)
                children.append(parent1.crossover(parent2))
                children.append(parent2.crossover(parent1))

            sub_population += children
            sub_population = self.select_survivors(sub_population, sub_size)

        self.solution = max(best_solutions)

    def select_survivors(self, population, size):
        survivors = population
        while len(survivors) > size:
            survivors = [
                chromossome for chromossome in survivors
                if random.randint(0, 100) <= chromossome.survive_chance
            ]
        return survivors
