from flask import Flask, render_template, send_from_directory
import os
file_path = os.path.dirname(__file__)
app = Flask(__name__)

# @app.route('/')
# def home():
#     return send_from_directory(root, "homepage.html")#homepage.html在html文件夹下
# app = Flask(__name__,static_url_path='')#修改静态文件夹的目录

@app.route('/index')
def index():
    data = {'nickname': '刘新宇'}  # fake user

    return render_template("login.html")


@app.route('/')
def home():
    return app.send_static_file('index.html')#homepage.html在static文件夹下

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)