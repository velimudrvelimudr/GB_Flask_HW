from blog.app import blog_app
from blog.models.database import db
from blog.models.user import User

from json import load
from time import sleep


blog_app.run(
    host='127.0.0.1',
    debug=True
)

""" Команды flask.  """

@blog_app.cli.command('init-db')
def init_db():
    """ Создание базы данных и таблиц согласно моделям.  """
    db.create_all()
    print('Команда init_db выполнена!')


@blog_app.cli.command('import_json_user')
def import_json_user():
    """ Импорт данных для модели User из json-файла.  """
    with open('db/users.json', 'r', encoding='utf-8') as f:
        ujs = load(f)
    
    for u in ujs:
        NewUser = User(u['user_name'], u['user_name'] + '@email.ru', firstname=u['first_name'], lastname=u['last_name'])
        db.session.add(NewUser)
        sleep(1)
    db.session.commit()
