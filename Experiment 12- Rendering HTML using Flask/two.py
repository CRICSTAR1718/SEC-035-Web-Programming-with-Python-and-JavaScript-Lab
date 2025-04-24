from flask import Flask, render_template
two = Flask(__name__)
@two.route('/')
def home():
    return render_template("two.html")
if __name__ == '__main__':
    two.run(debug=True)
