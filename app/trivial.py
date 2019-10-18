from eve import Eve
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import column_property

from eve_sqlalchemy import SQL
from eve_sqlalchemy.config import DomainConfig, ResourceConfig
from eve_sqlalchemy.validation import ValidatorSQL
from sql import Tasks, Base

app = Eve(auth=None, validator=ValidatorSQL, data=SQL)

# bind SQLAlchemy
db = app.data.driver
Base.metadata.bind = db.engine
db.Model = Base
db.create_all()

# Insert some example data in the db
if not db.session.query(Tasks).count():
    db.session.add_all([
        Tasks(name=u'Vaisselle', status=u'Todo'),
        Tasks(name=u'Linge', status=u'Todo'),
        Tasks(name=u'Ménage', status=u'Done')])
    db.session.commit()

app.run(debug=True, use_reloader=False)
