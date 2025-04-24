from flask import Flask, render_template
four= Flask(__name__)
@four.route('/')
def home():
    items = ["Apple", "Banana", "Cherry", "Date"]
    return render_template("four.html", items=items)
if __name__ == '__main__':
    four.run(debug=True)
