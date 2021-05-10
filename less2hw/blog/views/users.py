from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

users_bp = Blueprint('users_bp', __name__)

USERS = {
    1:'Маша',
    2:'Миша',
    3:'Паша'
}

@users_bp.route('/', endpoint='list')
def users_list():
    return render_template('users/list.html', users=USERS)

@users_bp.route('/<int:user_id>/', endpoint='details')
def user_details(user_id: int):
    try:
        user_name = USERS[user_id]
    except KeyError:
        raise NotFound(f'Пользователь #{user_id} Не существует.')
    return render_template('users/details.html', user_name=user_name, user_id=user_id)