from flask import Flask, request

blog_app = Flask(__name__)

@blog_app.route('/')
def main_page():
    return 'Моя страница!'

@blog_app.route('/<name>')
def hello_name(name: str):
    return f'Привет, {name}'

@blog_app.route('/user/')
def get_user():
    name = request.args.get('name')
    surname = request.args.get('surname')
    return f'Пользователь {name or "безымянный"}, {surname or "Безфамильный"}.'

@blog_app.route('/req/', methods=['POST', 'GET'])
def req_test():
    if request.method == "GET":
        return "Это был метод 'GET'."
    elif request.method == 'POST':
        return "Это был метод 'POST'."
