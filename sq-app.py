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
    
@app.route('/q1', methods=['GET','POST'])
def renderPage1():
    return render_template("sq-p1.html")
    
@app.route('/q2', methods=['GET','POST'])
def renderPage2():
    session["q1ans"]=request.form['q1ans']
    return render_template("sq-p2.html")
    
@app.route('/q3', methods=['GET', 'POST'])
def renderPage3():
    session["q2ans"]=request.form['q2ans']
    return render_template("sq-p3.html")

@app.route('/results', methods=['GET', 'POST'])
def renderResults():
    session["q3ans"]=request.form['q3ans']
    checkAnswers()
    return render_template("sq-results.html")
    
 
def checkAnswers():
    if session['q1ans']=="vehicles next to the broken line may pass":
        print("yas")
    else:
        print(":(")
#if session['qxans']does not equal qxcorrectans
    #show x/turn red
    #show correct answer
    
    
if __name__=="__main__":
    app.run(debug=False)