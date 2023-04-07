import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"]; 

@app.route('/')
def renderMain():
    return render_template('sqhome.html')
    
@app.route('/startOver')
def startOver():
    session.clear()
    return redirect(url_for('renderMain'))
    
@app.route('/q1')
def renderPage1():
    return render_template("sq-p1.html")
    
if __name__=="__main__":
    app.run(debug=False)