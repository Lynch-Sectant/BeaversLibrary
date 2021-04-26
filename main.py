from flask import Flask, render_template, redirect
import os
from data import db_session
from flask_wtf import FlaskForm
from forms.user import RegisterForm
from forms.book import RedactorForm
from flask_login import login_required
import flask_login
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')  # тест проги
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
        if len(form.text.data) <= 40000:
            length = 'короткий'
    elif len(form.text.data) < 40000 and len(form.text.data) <= 80000:
        length = 'средний'
    elif len(form.text.data) > 80000:
        length = 'длинный'
        book = db_session.Book(
            title=form.title.data,
            author=form.author.data,
            sinopsis=form.sinopsis.data,
            text=form.text.data,
            tag_from_length=length,
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
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
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
@login_required
def my_page():
    db_sess = db_session.create_session()
    if db_sess.query(db_session.Book).filter(db_session.Book.author == User.current_user).all():
        my_books = [i[1] for i in
                    db_sess.query(db_session.Book).filter(db_session.Book.author == User.current_user).all()]
        return render_template('profile.html', title='Моя страница', user_books=my_books)
    else:
        my_books = ['У вас нет книг']
        return render_template('profile.html', title='Моя страница')


def main():
    db_session.global_init('db.db')
    port = int(os.environ.get("PORT", 5000))
    app.run(host='127.0.0.1', port=port)


if __name__ == '__main__':
    main()

