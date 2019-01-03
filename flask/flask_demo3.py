from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class Config(object):
    DEBUG = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/flask_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True




app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = "roles"
    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.String(64), unique=True)
    us = db.relationship("User", backref="role")

    def __repr__(self):
        return "Role:%s" % self.name
class User(db.Model):
    __tablename__ = "users"
    id = db.column(db.Integer,primary_key = True)
    name = db.column(db.String(64),unique = True,index= True)
    email = db.column(db.String(64),unique = True)
    password = db.column(db.String(64))
    role_id = db.column(db.Integer,db.ForeignKey("roles.id"))

    def __repr__(self):
        return "User:%s"%self.name


@app.route("/", methods=["get", "post"])
def demo1():
    pass

def demo2():
    pass


if __name__ == '__main__':
    app.run()
