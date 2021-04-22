from flask import Flask
import os
from .forms.user import RegisterForm

app = Flask(__name__)

@app.route('/create_a_book', methods=['GET', 'POST'])
def new_book():
    form = UploadForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('upload.html', title='Добавить книгу', form=form)


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

@app.route('/my_page' methods=['GET', 'POST'])
def my_page():
    db_sess = db_session.create_session()
    if db_sess.query(Book).filter(Book.author == current_user).all():
        my_books = db_sess.query(Book).filter(Book.author == current_user).all()
        return render_template('profile.html', tilte='Моя страница')
    else:
        my_books = ['У вас нет книг']
        return render_template('profile.html', tilte='Моя страница')
    
def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
