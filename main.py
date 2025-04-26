from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/register', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template('register_form.html')
    elif request.method == 'POST':
        print(request.form.get('firstname'))
        print(request.form.get('surname'))
        print(request.form.get('midname'))
        print(request.form.get('city'))
        print(request.form.get('email'))
        print(request.form.get('phone'))
        print(request.form.get('extra'))
        print(request.form.get('role'))
        return "Форма отправлена"
    return None


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
