class Gene(object):

    def __init__(self, analyst, requirement):
        self.analyst = analyst
        self.requirement = requirement

    def __str__(self):
        return '{0} => {1}'.format(self.requirement.code, self.analyst.name)

    def __eq__(self, gene):
        return self.fitness == gene.fitness

    def __lt__(self, gene):
        return self.fitness < gene.fitness

    def __gt__(self, gene):
        return self.fitness > gene.fitness

    @property
    def fitness(self):
        experience = self.analyst.experience * 2.5
        availability = self.analyst.availability() * 10 / \
            self.analyst.max_requirements
        skill = self.analyst.skill_level_for(self.requirement)

        return (experience + availability + skill) / 3
