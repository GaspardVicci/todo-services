from eve_sqlalchemy.config import DomainConfig, ResourceConfig

from sql import Tasks

SQLALCHEMY_DATABASE_URI = 'postgresql://ernesti:nest@postgresql:5432/nestdb'
SQLALCHEMY_TRACK_MODIFICATIONS = False
RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
DEBUG = True

tasks = ResourceConfig(Tasks)

DOMAIN = DomainConfig({
    'tasks': tasks,
}).render()
