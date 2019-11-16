from flask import Flask, render_template, redirect, url_for
from flask_login import login_required,  current_user
from datetime import timedelta
from views import order_web, user_web, user_api, menu_web, another_web
from lib.auth import User, login_manager, admin_required


APP = Flask(__name__)
APP.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
APP.config['SECRET_KEY'] = "thisdhfiehi"

login_manager.init_app(APP)

def register_web():
    APP.register_blueprint(order_web.order_web, url_prefix='/order')
    APP.register_blueprint(user_web.user_web, url_prefix='/user')
    APP.register_blueprint(menu_web.menu_web, url_prefix='/menu')
    APP.register_blueprint(another_web.another_web, url_prefix='/')

def register_api():
    APP.register_blueprint(user_api.user_api, url_prefix='/api/user')

def run():
    register_web()
    register_api()
    APP.run(debug=True)

if __name__ == '__main__':
    run()