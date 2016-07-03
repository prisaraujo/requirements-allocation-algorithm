from constants import ANALYST_WORKLOAD_MULTIPLIER
from .enums import ANALYST_EXPERIENCE_CHOICES


class Analyst(object):

    def __init__(self, pk, name, experience, skills, workload):
        self.pk = pk
        self.name = name
        self.experience = experience
        self.skills = skills
        self.workload = workload
        self.requirements_to_analysis = []
        self.requirements_to_review = []
        self.speed_workload = workload * ANALYST_WORKLOAD_MULTIPLIER[self.experience]  # noqa

    @property
    def experience_text(self):
        return dict(ANALYST_EXPERIENCE_CHOICES)[self.experience]

    def skill_level_for(self, requirement):
        category = str(requirement.category)
        if category in self.skills:
            return self.skills[category]
        return 0
