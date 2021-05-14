from flask import Flask, request, render_template
from blog.views.users import users_bp
from blog.views.articles import articles_bp

blog_app = Flask(__name__)

blog_app.register_blueprint(users_bp, url_prefix='/users')
blog_app.register_blueprint(articles_bp, url_prefix='/articles')

@blog_app.route('/')
@blog_app.route('/<name>')
def main_page(name=None):
    if name:
        return render_template('index.html', name=name)
    else:
        return render_template('index.html')


