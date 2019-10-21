import os

from eve import Eve
from eve.methods.patch import patch_internal
from eve.methods.post import post_internal
from eve.render import send_response
from eve_sqlalchemy import SQL
from eve_sqlalchemy.validation import ValidatorSQL
from flask import request
from flask_migrate import Migrate
from sqlalchemy.ext.declarative import declarative_base

from sql import Base, Tasks

settings = os.path.join( os.path.dirname(__file__), "settings.py")

app = Eve(validator=ValidatorSQL, data=SQL, settings=settings)

db = app.data.driver
Base.metadata.bind = db.engine
db.Model = Base

Migrate(app, db)

@app.route('/task', methods=["PATCH", "POST"])
def task():
    print("request", request)

    if request.method == "PATCH":
        print("heelloooooo")
        return send_response("tasks", patch_internal("tasks", payload = request.json))
    return send_response("tasks", post_internal("tasks", request.json))

db.create_all()

if not db.session.query(Tasks).count():
    db.session.add_all([
        Tasks(name='Vaisselle', status='Todo'),
        Tasks(name='Linge', status='Todo'),
        Tasks(name='Ménage', status='Done')])
    db.session.commit()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
