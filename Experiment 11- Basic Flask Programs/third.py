from flask import Flask, render_template
third = Flask(__name__)
@third.route('/')
def home():
    return render_template('third.html', title="Flask Template Example")
if __name__ == '__main__':
    third.run(debug=True)
