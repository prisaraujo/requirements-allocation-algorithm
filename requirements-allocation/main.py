from allocation.core import Core
from utils import get_requirements
from utils import get_analysts
from utils import get_time


def main():
    # Simple Algorithm
    print('Starting algorithm: {}'.format(get_time()))
    core = Core(
        requirements=get_requirements(),
        analysts=get_analysts()
    )
    core.run()
    print('Stopping algorithm: {}\nResults:'.format(get_time()))
    print('Solution fitness: {}'.format(core.solution.fitness))
    for gene in core.solution.genes:
        print('{0} ({1})'.format(gene, gene.fitness))


if __name__ == '__main__':
    main()
