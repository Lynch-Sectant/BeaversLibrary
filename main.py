from flask import Flask, render_template, redirect
import os
from forms.user import RegisterForm
from forms.book import RedactorForm
from data import db_session
from flask_wtf import FlaskForm
import flask_login

app = Flask(__name__)


@app.route('/') # тест проги
def start():
    greeting = f'''<html>
        <head>
        <title>Привет, Марс!</title>
        </head>
        <body>
        <h1>Жди нас, Марс!</h1>
        <div>Вот она какая, красная планета</div>
        <body>
        </html>'''
    return greeting


@app.route('/redactor', methods=['GET', 'POST'])
def new_book():
    form = RedactorForm()
    if form.validate_on_submit():
        book = db_session.Book(
            title=form.title.data,
            author=form.author.data,
            sinopsis=form.sinopsis.data,
            text=form.text.data,
            tag=form.tag.data
        )
        db_session.add(book)
        db_session.commit()
        return redirect('/my_page')
    return render_template('profile.html', tilte='Моя страница', form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(db_session.User).filter(db_session.User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = db_session.User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/my_page', methods=['GET', 'POST'])
def my_page():
    db_sess = db_session.create_session()
    if db_sess.query(db_session.Book).filter(db_session.Book.author == db_session.User.current_user).all():
        my_books = db_sess.query(db_session.Book).filter(db_session.Book.author == db_session.User.current_user).all()
        return render_template('profile.html', tilte='Моя страница')
    else:
        my_books = ['У вас нет книг']
        return render_template('profile.html', tilte='Моя страница')


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
