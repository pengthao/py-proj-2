from cakeStore import app, db
from flask import render_template, redirect, request

app.app_context().push()

@app.route('/')
def home():
    return render_template('home.html')

if __name__=='__main__':
    app.run(debug=True)