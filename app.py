
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request
from templates import *
import os
import json

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/', methods=['GET', 'POST'])
# ‘/’ URL is bound with hello_world() function.
def main_page():
    password = request.form.get("password")
    if(password == "1990"):
        return render_template("mainpage.html")
    else:
        return render_template('login.html')

@app.route('/WOL')
def exec_CMD():
    os.system('etherwake -b 00:E0:0B:42:10:18 -i wlan0')
    dictionary = {'code':200, 'message':"OK"}
    jsonString = json.dumps(dictionary, indent=4)
    return jsonString

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()