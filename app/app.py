from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import settings

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://postgres:docker@db:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)


db.create_all()


@app.route('/')
def index():
    person = Person.query.first()
    return 'Hello ' + person.name


if __name__ == '__main__':
    app.run(debug=settings.FLASK_DEBUG,
            threaded=settings.FLASK_THREADED,
            port=7000)
