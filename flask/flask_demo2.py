from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo



class Config(object):
    DEBUG = True
    WTF_CSRF_ENABLED  = True



app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = "asdgjhkfgahgf"


class Register(FlaskForm):
    username = StringField("用户名",validators=[DataRequired("请输入用名")],render_kw={"placeholder":"请输入123"})
    password = PasswordField("密码",validators=[DataRequired("请输入密码")],render_kw={"placeholder":"请输入密码"})
    password2 = PasswordField("确认密码",validators=[DataRequired("请再次输入密码"),EqualTo(password,"两次密码不一致")] )
    submit = SubmitField("注册")

@app.route("/demo2",methods=["get","post"])
def demo2():
    registerform = Register()
    if registerform.validate_on_submit():
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        print(username,password,password2)
        return "success"
    else:
        if request.method == "post":
            flash("参数不完整")
    return render_template("flaskwtf_register.html",form = registerform)


# @app.route("/")
# def index():
#     my_str = "hello 程序员"
#     my_littleint = 10
#     my_list = [1, 2, 5]
#     my_dict = {"name": "tian"}
#     return render_template("index1.html", my_str=my_str, my_int=my_littleint, my_list=my_list, my_dict=my_dict)

#html自带表单
# @app.route("/demo1", methods=["get", "post"])
# def demo1():
#     if request.method == "post":
#         username = request.form.get("username")
#         password = request.form.get("password")
#         password2 = request.form.get("password2")
#         if not all([username, password, password2]):
#             flash("参数不足")
#         elif password != password2:
#             flash("两次输入密码不一致")
#         else:
#             print(username,password,password2)
#             return "success"
#     return render_template("login.html")




# @app.route("/demo1",methods=["get","post"])
# def demo1():



if __name__ == '__main__':
    app.run()
