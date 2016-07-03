import json
import datetime
from models.requirement import Requirement
from models.analyst import Analyst


def read_file(file_name):
    with open(file_name) as data_file:
        data = json.load(data_file)
        return data


def get_analysts():
    analysts = []
    for data in read_file('data/analysts.json'):
        analysts.append(Analyst(
            pk=data['pk'],
            name=data['name'],
            experience=data['experience'],
            skills=data['skills'],
            workload=data['workload'],
        ))
    return analysts


def get_requirements():
    requirements = []
    for data in read_file('data/requirements.json'):
        requirements.append(Requirement(
            pk=data['pk'],
            code=data['code'],
            description=data['description'],
            req_type=data['type'],
            complexity=data['complexity'],
            category=data['category'],
            analyst=data['analyst']
        ))
    return requirements


def get_time():
    now = datetime.datetime.now()
    return now.strftime('%d/%m/%Y %H:%M:%S %f')
