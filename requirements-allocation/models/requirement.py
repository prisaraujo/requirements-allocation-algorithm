from datetime import datetime
from constants import REQUIREMENT_WORK_TIME
from .enums import RequirementStatusEnum
from .enums import RequirementCategoryEnum
from .enums import RequirementComplexityEnum
from .enums import REQUIREMENT_STATUS_CHOICES
from .enums import REQUIREMENT_CATEGORY_CHOICES
from .enums import REQUIREMENT_COMPLEXITY_CHOICES


class Requirement(object):

    def __init__(self, pk, code, description, req_type, complexity, category,
                 analyst):
        self.pk = pk
        self.code = code
        self.description = description
        self.type = req_type
        self.complexity = complexity
        self.category = category
        self.analyst = analyst
        self.analysis_date = datetime.now()
        self.reviewer = None
        self.review_date = None
        self.status = RequirementStatusEnum.ANALYSED
        self.work_time = REQUIREMENT_WORK_TIME[self.complexity]

    def __eq__(self, req):
        self.complexity = req.complexity

    def __lt__(self, req):
        self.complexity < req.complexity

    def __gt__(self, req):
        self.complexity > req.complexity

    @property
    def complexity_text(self):
        return dict(REQUIREMENT_COMPLEXITY_CHOICES)[self.complexity]

    @property
    def category_text(self):
        return dict(REQUIREMENT_CATEGORY_CHOICES)[self.category]

    @property
    def status_text(self):
        return dict(REQUIREMENT_STATUS_CHOICES)[self.status]

    def send_to_review(self, reviewer):
        self.reviewer = reviewer
        self.status = RequirementStatusEnum.REVIEWING
