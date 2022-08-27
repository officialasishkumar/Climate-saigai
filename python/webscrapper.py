from flask import Flask, render_template


app = Flask(__name__)
name = 'hello'
@app.route('/home')
def home():
    return render_template('home.html', person=name)


if __name__ == "__main__":
    app.run()