# this looks in the flask module -- looks in virtual environment (lib)!
from flask import Flask, render_template, session, request, redirect, flash
#Session = a dictionay that is accessible from page to page.
#Flask, core property of the flask module - it allows us to run the server.
#render_template - looks in root folder, for a subfolder named templates, and then looks into this for a name that matches what we pass it!
#request - Generates an object that is then passed to the server (allows user to request stuff from server e.g. pass in form info!)
#redirect - let's us send a 'get' type request internal to server
#flash - stores one-time reusable data.

# imports the entire random module
import random
# what is app???
app = Flask(__name__)
app.secret_key = "I<3SecretKeys"
# what does @ do??? Decorator - says the next thing it sees, belongs to it.
@app.route('/', methods = ['GET','POST'])
def index():
    # request.form  == info from 'post' method
    # request.get
    if 'number' not in session:
        session['number'] = random.randint(1,100)
    if request.method == 'POST':
        if session['number'] == int(request.form['guess']):
            del session['guess']
            # session.pop('guess')
            # session.clear() gets rid of all session
            # session['guess'] = False
            print 'WINNING'
        elif session['number'] > int(request.form['guess']):
            print 'GUESS TOO LOW'
        else:
            print 'GUESS TOO HIGH'
        return render_template('index.html', guess_result = "WINNING")
    return render_template('index.html')

app.run(debug = True, port = 8000)
