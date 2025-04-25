from flask import Flask, render_template, request, redirect, url_for

# Jinja 2 template engine is used by Flask to render HTML templates

app = Flask(__name__) # Create a Flask application instance, act as the WSGI application

@app.route('/') # Define a route for the root URL

def hello_world():
    return '<html><body><h1>FlASK 101: Welcome to the Flask application!</h1><p>This is a simple web server.</p></body></html>'
 # Return a welcome message

@app.route('/index',methods=['GET']) # Define a route for the root URL
def index():
    return render_template('index.html') # Render the index.html template

@app.route('/about') # Define a route with a variable part
def about():
    return render_template('about.html')


# variable rule
@app.route('/success/<score>')
def success(score):
    res =''
    if int(score) >= 50:
        res = 'You have passed the exam'
    else:
        res = 'You have failed the exam' 
    return render_template('result.html', result=res, score=score)

@app.route('/successres/<int:score>')
def successres(score):
    res =''
    if score >= 50:
        res = 'You have passed the exam'
    else:
        res = 'You have failed the exam'
    exp = {'score': score, 'result': res} 
    return render_template('result1.html', result=exp, score=score)

@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result.html', results=score)

@app.route('/fail/<score>')
def fail(score):
    return render_template('result.html', results=score)

@app.route('/submit',methods=['GET','POST'])
def submit():
    totalScore = 0
    if request.method == 'POST':
        science = float(request.form['Science'])
        math = float(request.form['Math'])
        english = float(request.form['English'])
        hindi = float(request.form['Hindi'])
        datascience = float(request.form['Datascience'])
        totalScore = (science + math + english + hindi + datascience) / 5
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres', score=totalScore))
        


if __name__ == '__main__':
    app.run(debug=True) # host and port are default
