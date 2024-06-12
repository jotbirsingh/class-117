# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Jotbir singh" # write your name
    age = "17" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/home2")
def home2():
    return "father's webpage"
# define the route to mother webpage
@app.route("/home3")
def home3():
    return "mother's webpage"

# define the route to friends webpage
@app.route("/home4")
def home4():
    return "friends webpage"
# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
