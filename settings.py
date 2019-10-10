from eve_sqlalchemy.config import DomainConfig, ResourceConfig
from sql import Tasks

SQLALCHEMY_DATABASE_URI = 'postgresql://gaspard:glaise@localhost:5432/'
SQLALCHEMY_TRACK_MODIFICATIONS = False
RESOURCE_METHODS = ['GET', 'POST']
DEBUG = True


DOMAIN = DomainConfig({
    'tasks': ResourceConfig(Tasks),
}).render()

