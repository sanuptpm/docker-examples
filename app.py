import os
from flask import Flask


app = Flask(__name__)

SECRET_KEY = os.environ.get("SECRET_KEY")

@app.route("/")
def hello():
    return "Flask inside Docker!! Hello"

@app.route("/env")
def evnshow():
    if SECRET_KEY:
      return "Remote address : "  + SECRET_KEY
    else:
      return 'Remote address not set'

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=4000)