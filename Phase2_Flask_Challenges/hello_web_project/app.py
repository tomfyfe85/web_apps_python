import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)


# == Your Routes Here ==
@app.route("/hello", methods=["GET"])
def get_hello():
    return "Hello!!!!!!!"


@app.route("/hello", methods=["POST"])
def post_hello():
    return "HELLLOOOO VIA POST"


@app.route("/greet", methods=["GET"])
# curl 'http://localhost:5001/greet?person=Tom'
def get_greet():
    name = request.args["person"]
    return f"HELLO THERE {name}!\n"
 
@app.route("/greet", methods=["POST"])
# curl -X POST -d "person=TOM" http://localhost:5001/greet
def post_greet():
    print(request.form)
    name = request.form['person']
    return f"HELLO THERE {name}\n"


# == Example Code Below ==


# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route("/emoji", methods=["GET"])
def get_emoji():
    return ":)"


# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes

apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5001)))
