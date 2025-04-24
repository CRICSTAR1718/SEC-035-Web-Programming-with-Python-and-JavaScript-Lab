from flask import Flask, request, render_template
fourth= Flask(__name__)
@fourth.route('/')
def form():
    return render_template('fourth.html')
@fourth.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return f"Hello, {name}! Welcome to Flask."
if __name__ == '__main__':
    fourth.run(debug=True)
