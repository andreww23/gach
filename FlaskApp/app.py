from flask import Flask, render_template
from data import db_session
from forms.user import RegisterForm
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        db_sess.add(user)
        db_sess.commit()
    return render_template('register.html', title='Регистрация', form=form)


if __name__ == "__main__":
    db_session.global_init("db/blogs.db")
    app.run()