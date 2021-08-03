from flask import Flask, render_template
from flaskext.mysql import MySQL


app = Flask(__name__)
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'localhost'
#app.config['MYSQL_PASSWORD'] = 'localhost'

@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")




if __name__ == '__main__':
    app.run(debug=True)
