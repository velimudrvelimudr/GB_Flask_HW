from flask import Blueprint, render_template
from json import load
from werkzeug.exceptions import NotFound

users_bp = Blueprint('users_bp', __name__)

def load_users():
    with open('db/users.json', 'r', encoding='utf-8') as     f:
        return load(f)

ujs = load_users()

@users_bp.route('/', endpoint='list')
def users_list():
    return render_template('users/list.html', users=ujs)

@users_bp.route('/<int:user_id>/', endpoint='details')
def user_details(user_id: int):
    user = [u for u in ujs if u['id'] == int(user_id)][0]
    return render_template('users/details.html', user=user)