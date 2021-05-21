from flask import Blueprint, render_template, request, redirect, url_for
from flask_login  import LoginManager, login_user, logout_user, login_required, current_user
from blog.models.user import User

auth_bp = Blueprint('auth_bp', __name__)
login_manager = LoginManager()
login_manager.view = 'auth_bp.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).one_or_none()


@login_manager.unauthorized_handler
def  unauthorized():
    return redirect(url_for('auth_bp.login'))


__all__ = [
    'login_manager',
    'auth_bp'
]

@auth_bp.route('/login', methods=['GET', 'POST'], endpoint='login')
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    
    username = request.form.get('username')
    if not username:
        return render_template('auth/login.html', error='Имя пользователя не передано')

    user = User.query.filter_by(user_name=username).one_or_none()
    if user is None:
        return render_template('auth/login.html', error=f'Пользователь {username!r} не найден!')
    
    login_user(user)
    return redirect(url_for('index', user_id=user.id))


@auth_bp.route('/logout', endpoint='logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@auth_bp.route('/secret/')
@login_required
def secret():
    return f'Сверхсекретная информация для {current_user.user_name}!'
