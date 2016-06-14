from algorithms.simple import SimpleAlgorithm
from algorithms.genetic import GeneticAlgorithm
from allocation.core import Core
from utils import get_requirements
from utils import get_analysts
from utils import get_time


def main():
    # Simple Algorithm
    print('Starting simple algorith: {}'.format(get_time()))
    core = Core(
        algorithm=SimpleAlgorithm,
        requirements=get_requirements(),
        analysts=get_analysts()
    )
    core.run()
    print('Stoping simple algorithm: {}\nResults:'.format(get_time()))

    for gene in core.selected_genes:
        print('{0} ({1})'.format(gene, gene.fitness))

    print('')

    # Genetic Algorithm
    print('Starting genetic algorith: {}'.format(get_time()))
    core = Core(
        algorithm=GeneticAlgorithm,
        requirements=get_requirements(),
        analysts=get_analysts()
    )
    core.run()
    print('Stoping genetic algorithm: {}\nResults:'.format(get_time()))

    for gene in core.selected_genes:
        print('{0} ({1})'.format(gene, gene.fitness))


if __name__ == '__main__':
    main()
