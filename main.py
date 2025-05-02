from flask import Flask, render_template, flash
from flask import request
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/users.db")


@app.route('/register', methods=['POST', 'GET'])
def register_form():
    if request.method == 'GET':
        return render_template('register_form.html')
    elif request.method == 'POST':
            email = request.form.get('email')
            phone = request.form.get('phone')
            db_sess = db_session.create_session()
            check_email_occupicy = db_sess.query(User).filter(User.email == email).first()
            check_phone_occupicy = db_sess.query(User).filter(User.phone == phone).first()
            if check_email_occupicy or check_phone_occupicy:
                flash('Аккаунт с указанным email или телефоном уже зарегистрирован.', 'danger')
                return render_template('register_form.html',
                                       surname=request.form.get('surname'),
                                       firstname=request.form.get('firstname'),
                                       midname=request.form.get('midname'),
                                       city=request.form.get('city'),
                                       email=request.form.get('email'),
                                       phone=request.form.get('phone'),
                                       pswd=request.form.get('password'))
            else:
                user = User()
                user.first_name = request.form.get('firstname')
                user.surname = request.form.get('surname')
                user.midname = request.form.get('midname')
                user.city = request.form.get('city')
                user.email = email
                user.phone = phone
                user.role = request.form.get('role')
                user.pswd = request.form.get('password')
                user.extra = request.form.get('extra')
                db_sess.add(user)
                db_sess.commit()
                return render_template('test_lk.html',
                        surname=request.form.get('surname'),
                        firstname=request.form.get('firstname'),
                        midname=request.form.get('midname'),
                        city=request.form.get('city'),
                        email=request.form.get('email'),
                        phone=request.form.get('phone'),
                        pswd=request.form.get('password'),
                        role=request.form.get('role'),
                        extra=request.form.get('extra'))
    return None

@app.route('/enter_with_email', methods=['POST', 'GET'])
def enter_with_email_form():
    if request.method == 'GET':
        return render_template('enter_with_email.html')
    elif request.method == 'POST':
        email = request.form.get('email')
        pswd = request.form.get('password')
        db_sess = db_session.create_session()
        check_account_data = db_sess.query(User).filter(User.email == email, User.pswd == pswd).first()
        if not check_account_data:
            flash('Неправильно введены почта или пароль!', 'danger')
            return render_template('enter_with_email.html', email=email, pswd=pswd)
        else:
            return render_template('test_lk.html',
                                   surname=check_account_data.surname,
                                   firstname=check_account_data.first_name,
                                   midname=check_account_data.midname,
                                   city=check_account_data.city,
                                   email=check_account_data.email,
                                   phone=check_account_data.phone,
                                   pswd=check_account_data.pswd,
                                   role=check_account_data.role,
                                   extra=check_account_data.extra)
    return None

@app.route('/enter_with_phone', methods=['POST', 'GET'])
def enter_with_phone_form():
    if request.method == 'GET':
        return render_template('enter_with_phone.html')
    elif request.method == 'POST':
        phone = request.form.get('phone')
        pswd = request.form.get('password')
        db_sess = db_session.create_session()
        check_account_data = db_sess.query(User).filter(User.phone == phone, User.pswd == pswd).first()
        if not check_account_data:
            flash('Неправильно введены телефон или пароль!', 'danger')
            return render_template('enter_with_phone.html', email=phone, pswd=pswd)
        else:
            return render_template('test_lk.html',
                                   surname=check_account_data.surname,
                                   firstname=check_account_data.first_name,
                                   midname=check_account_data.midname,
                                   city=check_account_data.city,
                                   email=check_account_data.email,
                                   phone=check_account_data.phone,
                                   pswd=check_account_data.pswd,
                                   role=check_account_data.role,
                                   extra=check_account_data.extra)
    return None


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
