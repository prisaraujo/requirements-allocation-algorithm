import random


class GeneticAlgorithm(object):

    def __init__(self, requirements, analysts):
        self.analysts = analysts
        self.requirements = requirements

    def select_gene(self, population):
        sub_population = population.genes
        sub_size = len(sub_population)

        for i in range(100):
            best_gene = max(sub_population)
            if best_gene.fitness >= 8:
                break

            for i in range(sub_size):
                parent1 = random.choice(sub_population)
                parent2 = random.choice(sub_population)
                sub_population.append(
                    self.mutate_gene(parent1.crossover(parent2))
                )
                sub_population.append(
                    self.mutate_gene(parent2.crossover(parent1))
                )

            sub_population = self.select_survivor(sub_population, sub_size)

        return max(sub_population)

    def select_survivor(self, population, size):
        return sorted(population, reverse=True)[:size]

    def mutate_gene(self, gene):
        if random.randint(0, 100) > 75:
            gene.analyst = random.choice(self.analysts)
        return gene
