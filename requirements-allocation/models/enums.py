class RequirementComplexityEnum(object):

    LOW = 0
    MEDIUM = 1
    HIGH = 2


REQUIREMENT_COMPLEXITY_CHOICES = (
    (RequirementComplexityEnum.LOW, 'Low'),
    (RequirementComplexityEnum.MEDIUM, 'Medium'),
    (RequirementComplexityEnum.HIGH, 'High'),
)


class RequirementCategoryEnum(object):

    BUSINESS = 0
    QUALITY = 1
    SECURITY = 2
    USABILITY = 3
    RELIABILITY = 4
    FUNCTIONALITY = 5
    PERFORMANCE = 6
    SUPPORTABILITY = 7


REQUIREMENT_CATEGORY_CHOICES = (
    (RequirementCategoryEnum.BUSINESS, 'Business'),
    (RequirementCategoryEnum.QUALITY, 'Quality'),
    (RequirementCategoryEnum.SECURITY, 'Security'),
    (RequirementCategoryEnum.USABILITY, 'Usability'),
    (RequirementCategoryEnum.RELIABILITY, 'Reliability'),
    (RequirementCategoryEnum.FUNCTIONALITY, 'Functionality'),
    (RequirementCategoryEnum.PERFORMANCE, 'Performance'),
    (RequirementCategoryEnum.SUPPORTABILITY, 'Supportability')
)


class RequirementStatusEnum(object):

    ANALYSED = 0
    REVIEWING = 1
    REVIWED = 2


REQUIREMENT_STATUS_CHOICES = (
    (RequirementStatusEnum.ANALYSED, 'Analysed'),
    (RequirementStatusEnum.REVIEWING, 'Reviewing'),
    (RequirementStatusEnum.REVIWED, 'REVIWED')
)


class AnalystExperienceChoices(object):

    ENTRY_LEVEL = 1
    JUNIOR = 2
    PAYROLL = 3
    SENIOR = 4


ANALYST_EXPERIENCE_CHOICES = (
    (AnalystExperienceChoices.ENTRY_LEVEL, 'Entry Level'),
    (AnalystExperienceChoices.JUNIOR, 'Junior'),
    (AnalystExperienceChoices.PAYROLL, 'Payroll'),
    (AnalystExperienceChoices.SENIOR, 'Senior')
)
