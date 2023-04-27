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
    check = checkAnswers()
    return render_template("sq-results.html", c1=check[0], c2=check[1], c3=check[2], score=check[3])
    
 
def checkAnswers():
    score = 0
    if session['q1ans']=="vehicles next to the broken line may pass":
        c1 = "That's correct!"
        score = score + 1
    else:
        c1 = "That's incorrect. The correct answer for question 1 was 'vehicles next to the broken line may pass.'"
    if session['q2ans']=="at all times":
        c2 = "That's correct!"
        score = score + 1
    else:
        c2 = "That's incorrect. The correct answer for question 2 was 'at all times.'"
    if session['q3ans']=="when turning (within 200 ft of an intersection)":
        c3 = "That's correct!"
        score = score + 1
    else:
        c3 = "That's incorrect. The correct answer for question 3 was 'when turning (within 200 ft of an intersection).'"
    return c1, c2, c3, score

if __name__=="__main__":
    app.run(debug=False)
