from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/register', methods=['POST', 'GET'])
def register_form():
    if request.method == 'GET':
        return render_template('register_form.html')
    elif request.method == 'POST':
        print(request.form.get('firstname'))
        print(request.form.get('surname'))
        print(request.form.get('midname'))
        print(request.form.get('city'))
        print(request.form.get('email'))
        print(request.form.get('phone'))
        print(request.form.get('role'))
        print(request.form.get('password'))
        print(request.form.get('extra'))
        return "Форма отправлена"
    return None

@app.route('/enter_with_email', methods=['POST', 'GET'])
def enter_with_email_form():
    if request.method == 'GET':
        return render_template('enter_with_email.html')
    elif request.method == 'POST':
        print(request.form.get('email'))
        print(request.form.get('password'))
        return "Форма отправлена"
    return None

@app.route('/enter_with_phone', methods=['POST', 'GET'])
def enter_with_phone_form():
    if request.method == 'GET':
        return render_template('enter_with_phone.html')
    elif request.method == 'POST':
        print(request.form.get('phone'))
        print(request.form.get('password'))
        return "Форма отправлена"
    return None


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
