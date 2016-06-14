class SimpleAlgorithm(object):

    def __init__(self, requirements, analysts):
        self.analysts = analysts
        self.requirements = requirements

    def select_gene(self, population):
        return max(population.genes)
