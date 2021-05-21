from flask import Blueprint, render_template
from blog.models.user import User
# from blog.models.database import db
# from json import load

users_bp = Blueprint('users_bp', __name__)


""" def load_users():
    with open('db/users.json', 'r', encoding='utf-8') as     f:
        return load(f)


ujs = load_users()
 """


@users_bp.route('/', endpoint='list')
def users_list():
    users = User.query.all()
    return render_template('users/list.html', users=users)


@users_bp.route('/<int:user_id>/', endpoint='details')
def user_details(user_id: int):
    user = User.query.filter(User.id==user_id).one()
    return render_template('users/details.html', user=user)
