from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("COVID.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=False, port=80)
#
# def appliaction():
#     app = Flask(__name__)
#
#     return app
#
# if __name__ == '__main__':
#     APP = appliaction()
#     APP.run(host='127.0.0.1', debug=False, port=80)
