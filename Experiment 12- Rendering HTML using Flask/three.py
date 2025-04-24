from flask import Flask, render_template
three = Flask(__name__)
@three.route('/')
def home():
    user = "John Doe"
    return render_template("three.html", username=user)
if __name__ == '__main__':
    three.run(debug=True)
