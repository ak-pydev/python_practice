from flask import Flask

app = Flask(__name__) # Create a Flask application instance, act as the WSGI application

@app.route('/') # Define a route for the root URL

def welcome():
    return 'FlASK 101: Welcome to the Flask application!. This is a simple web server.' # Return a welcome message

if __name__ == '__main__':
    app.run(debug=True) # host and port are default
