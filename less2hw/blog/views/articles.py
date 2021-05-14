from flask import Blueprint, render_template

from json import load
from werkzeug.exceptions import NotFound

articles_bp = Blueprint('articles_bp', __name__)

def load_articles():
    with open('db/articles.json', 'r', encoding='utf-8') as f:
        return load(f)

ajs = load_articles()

def load_users():
    with open('db/users.json', 'r', encoding='utf-8') as f:
        return load(f)

ujs = load_users()

@articles_bp.route('/', endpoint='list')
@articles_bp.route('/u/<int:user_id>/', endpoint='list')
def articles_list(user_id: int=None):
    if user_id:
        au = [a for a in ajs if a['author'] == user_id]
        user = [u['user_name'] for u in ujs if u['id'] == user_id][0]
        title = f'Статьи пользователя {user}'
    else:
        au = ajs
        title = 'Список статей'
        user = None
    return render_template('articles/list.html', title=title, user=user, articles=au)

@articles_bp.route('/a/<article_id>', endpoint='article_page')
def article_page(article_id: int):
    art = [a for a in ajs if a['id'] == int(article_id)][0]
    user = [u for u in ujs if u['id'] == art['author']][0]
    return render_template('articles/article.html', article=art, user=user)

