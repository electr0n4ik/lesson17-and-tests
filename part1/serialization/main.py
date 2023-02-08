# Задана модель Role, напишите схему и используйте
# сериализацию внутри функции serialize так,
# чтобы она возвращала JSON данные такого типа:
#
# {
#    "name": "buratino",
#    "id": 1
# }

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
app.url_map.strict_slashes = False
db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


db.create_all()
role = Role(id=1, name="buratino")

with db.session.begin():
    db.session.add(role)


class RoleSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()



def serialize():
    book_schema = RoleSchema()
    result = Role.query.get(1)
    return book_schema.dumps(result)



if __name__ == "__main__":
    print(json.dumps(serialize(), indent=4))
