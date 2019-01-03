from flask import Flask, request, jsonify, redirect, url_for, abort, make_response, session


class Config(object):
    DEBUG = True


app = Flask(__name__)

app.config.from_object(Config)
app.secret_key = 'sghsdfjkghsdkjghsjk'

@app.route("/demo1")
def demo1():
    return "hello,word"

@app.route("/demo2",methods=["get","post"])
def demo2():
    return request.method

@app.route("/demo3")
def demo3():
    dict_info = {"name":"Tom","age":25}
    return jsonify(dict_info)

@app.route("/demo4")
def demo4():
    return redirect(url_for("index"))

@app.route('/demo5')
def demo5():
    return '状态码为1231564654 666', 888

@app.route('/demo6')
def demo6():
    abort(500)

@app.errorhandler(500)
def internal_server_error(e):
    return '服务器搬家了'

@app.route('/demo7')
def demo7():
    resp = make_response("hello,python")
    resp.set_cookie("username","Tom",max_age=3600)
    return resp

@app.route('/demo8')
def demo8():
    resp = request.cookies.get("username")
    return resp

@app.route('/demo9')
def index1():
    session['username'] = 'itcast'
    return redirect(url_for('index'))

@app.route('/')
def index():
    return session.get('username')

if __name__ == '__main__':
    app.run()