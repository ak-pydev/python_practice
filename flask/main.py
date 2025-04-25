from flask import Flask, render_template, request 

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

@app.route('/form',methods=['GET','POST']) 

def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f" Hello {name}, your email is {email}."
    return render_template('form.html')

@app.route('/submit',methods=['GET','POST']) 

def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f" Hello {name}, your email is {email}."
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True) # host and port are default
