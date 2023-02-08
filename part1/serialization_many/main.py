# Задана модель Role,
# напишите схему и сериализацию так,
# чтобы функция serialize() возвращала
# JSON данные такого типа:
#
#
#   [
#     {
#       "name": "user",
#       "id": 1
#     },
#     {
#       "name": "admin",
#       "id": 2
#     },
#     {
#       "name": "pupil",
#       "id": 3
#     }
#   ]
#
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from marshmallow import fields, Schema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
app.url_map.strict_slashes = False
db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


roles = [
    Role(id=1, name='user'),
    Role(id=2, name='admin'),
    Role(id=3, name='pupil')
]

db.create_all()

with db.session.begin():
    db.session.add_all(roles)


class RoleSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


def serialize():
    book_schema = RoleSchema(many=True)
    # result = Role.query.get(1)
    return book_schema.dumps(roles)


if __name__ == "__main__":
    print(json.dumps(serialize(), indent=2))

