from .enums import ANALYST_EXPERIENCE_CHOICES


class Analyst(object):

    def __init__(self, pk, name, experience, skills, max_requirements):
        self.pk = pk
        self.name = name
        self.experience = experience
        self.skills = skills
        self.max_requirements = max_requirements
        self.requirements_to_analysis = []
        self.requirements_to_review = []

    @property
    def experience_text(self):
        return dict(ANALYST_EXPERIENCE_CHOICES)[self.experience]

    def availability(self):
        working_reqs = len(
            self.requirements_to_analysis + self.requirements_to_review)
        return self.max_requirements - (working_reqs)

    def skill_level_for(self, requirement):
        category = str(requirement.category)
        if category in self.skills:
            return self.skills[category]
        return 0
