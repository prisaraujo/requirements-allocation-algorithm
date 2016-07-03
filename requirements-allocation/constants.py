from models.enums import RequirementComplexityEnum
from models.enums import AnalystExperienceChoices


REQUIREMENT_WORK_TIME = {
    RequirementComplexityEnum.LOW: 2,
    RequirementComplexityEnum.MEDIUM: 3,
    RequirementComplexityEnum.HIGH: 5
}

ANALYST_WORKLOAD_MULTIPLIER = {
    AnalystExperienceChoices.ENTRY_LEVEL: 0.5,
    AnalystExperienceChoices.JUNIOR: 1,
    AnalystExperienceChoices.PAYROLL: 2,
    AnalystExperienceChoices.SENIOR: 3
}
