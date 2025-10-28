from flask import Flask, render_template, url_for, redirect, flash, request
from telegramto import send_tg

app = Flask(__name__)

app.secret_key = 'mysecretkey'

@app.get('/')
@app.get('/landing')
def landing():
    return render_template('index.j2')

@app.get('/contacts')
def contacts():
    return render_template('contacts.j2')

@app.get('/team/<doctor>')
def doctor_page(doctor):
    template = f'doctors/{doctor}.j2'
    try:
        return render_template(template)
    except:
        return redirect(url_for('team'))

@app.get('/team')
def team():
    return render_template('team.j2')

@app.get('/eliner')
def eliner():
    return render_template('eliner.j2')

@app.get('/articles/<article>')
def article_page(article):
    template = f'articles/{article}.j2'
    try:
        return render_template(template)
    except:
        return redirect(url_for('landing'))


@app.get('/success')
def success():
    return render_template('success.j2')


@app.post('/send')
def send():
    name = request.form.get('name')
    phone = request.form.get('phone')
    comment = request.form.get('comment')
    send_tg(
        {
            'name': name,
            'phone': phone,
            'comment': comment
        }
    )
    flash('Сообщение отправлено')
    return redirect(url_for('success'))


if __name__ == "__main__":
    app.run(debug=True, port='5400', use_reloader=False)