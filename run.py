from eve import Eve
from eve_sqlalchemy import SQL
from eve_sqlalchemy.validation import ValidatorSQL
from sqlalchemy.ext.declarative import declarative_base
from sql import Tasks, Base

app = Eve(validator=ValidatorSQL, data=SQL)

db = app.data.driver
Base.metadata.bind = db.engine
db.Model = Base

db.create_all()

if not db.session.query(Tasks).count():
    db.session.add_all([
        Tasks(name=u'Vaisselle', status=u'Todo'),
        Tasks(name=u'Linge', status=u'Todo'),
        Tasks(name=u'Ménage', status=u'Done')])
    db.session.commit()
# db.session.add_all([
#         People(firstname=u'George', lastname=u'Washington'),
#         People(firstname=u'John', lastname=u'Adams'),
#         People(firstname=u'Thomas', lastname=u'Jefferson')])

if __name__ == '__main__':
    app.run(debug=True)
