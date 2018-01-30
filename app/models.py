from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer)

    def to_row(self):
        return "<tr><td>{}</td><td>{}</td></tr>".format(self.name, self.age)