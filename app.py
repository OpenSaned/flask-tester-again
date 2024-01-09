from flask import Flask
from flask import render_template
from modules import modules
app = Flask(__name__)

@app.route("/")
def index():
    hello = modules.hello()
    content = modules.content()
    return render_template("index.html", hello=hello, content=content)

if __name__ == "__main__":
    app.run(debug=True)
