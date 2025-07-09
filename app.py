from flask import Flask, render_template, url_for, redirect, flash, request

app = Flask(__name__)

app.secret_key = 'mysecretkey'

@app.get('/')
@app.get('/landing')
def landing():
    return render_template('index.html')

@app.get('/contacts')
def contacts():
    return render_template('contacts.html')

@app.get('/team/daria')
def daria():
    return render_template('doctor-daria.html')

@app.get('/team/anastasia')
def anastasia():
    return render_template('doctor-anastasia.html')

@app.get('/team/jadan-igor')
def igor():
    return render_template('doctor-igor.html')

@app.get('/team/jadan-anastasia')
def jadan():
    return render_template('doctor-jadan.html')

@app.get('/team')
def team():
    return render_template('team.html')

@app.get('/client')
def client():
    return render_template('client.html')

@app.get('/eliner')
def eliner():
    return render_template('eliner.html')

@app.get('/success')
def success():
    return render_template('success.html')



if __name__ == "__main__":

    app.run(debug=True, port='8000')