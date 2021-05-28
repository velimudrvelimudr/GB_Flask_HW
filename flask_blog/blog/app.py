from flask import Flask, render_template
from blog.views.users import users_bp
from blog.views.articles import articles_bp
from blog.views.auth import auth_bp, login_manager
from blog.models.database import db
from flask_migrate import Migrate
import os

blog_app = Flask(__name__)

cfg_name = os.environ.get('CONFIG_NAME') or 'DevConfig'
blog_app.config.from_object(f'blog.config.{cfg_name}')

migrate = Migrate(blog_app, db, compare_type=True)

blog_app.register_blueprint(users_bp, url_prefix='/users')
blog_app.register_blueprint(articles_bp, url_prefix='/articles')
blog_app.register_blueprint(auth_bp, url_prefix='/auth')

# blog_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
# blog_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# blog_app.config['SECRET_KEY'] = 'vstavayproklyatyemzakleymlyonnyiy1917'


db.init_app(blog_app)
login_manager.init_app(blog_app)


@blog_app.route('/', endpoint='index')
@blog_app.route('/<name>', endpoint='index')
def main_page(name=None):
    if name:
        return render_template('index.html', name=name)
    else:
        return render_template('index.html')
