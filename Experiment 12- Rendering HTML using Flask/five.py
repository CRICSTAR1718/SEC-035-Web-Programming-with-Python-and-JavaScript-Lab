from flask import Flask, render_template, request
five = Flask(__name__)
@five.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return render_template("five(one).html", name=name)
    return render_template("five(two).html")
if __name__ == '__main__':
    five.run(debug=True)
