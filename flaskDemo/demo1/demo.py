from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/puppy/<name>')
def pup_name(name):
    return render_template('puppies.html', name=name)


if __name__== '__main__':
    app.run(debug=True)



'''@app.route('/')
def index():
    return "<h1>Hello Puppy!</h1>"

@app.route('/info')
def info():
    return "<h1>Puppies are cute!</h1>"


@app.route('/puppy/<name>')
def puppy(name):
    return "<h1>100th letter: {}</h1>".format(name[100])

@app.route('/puppy_latin/<name>')
def puppy_latin(name):

    if name[-1] =='y':
        name2 = name[:-1]+'iful'
        return f"<h1>Hi {name}! Your puppy latin last name is {name2}</h1>"
    else:
        name2 = name[:-1]+'y'
        return f"<h1>Hi {name}! Your puppy latin last name is {name2}</h1>"
'''

'''@app.route('/')
def index():
    user_logged_in = False
    return render_template('index.html', user_logged_in=user_logged_in)'''