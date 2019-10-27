from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from datetime import timedelta


APP = Flask(__name__)
APP.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
APP.config['SECRET_KEY'] = "thisdhfiehi"
login_manager = LoginManager()
login_manager.init_app(APP)

class User(UserMixin):
    pass

@login_manager.user_loader
def user_loader(email):
    user = User()
    user.id = "admin" 
    return user

@APP.route('/login', methods=['GET'])
def login():
    user = User()
    user.id = "admin"
    login_user(user)
    return redirect(url_for('menu'))

@APP.route('/logout', methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for('menu'))

@APP.route('/')
def menu():
    auth = current_user.is_authenticated
    return render_template('menu.html', auth=auth)

@APP.route('/cart')
def cart():
    auth = current_user.is_authenticated
    return render_template('cart.html', auth=auth)

@APP.route('/profile/<isMe>', methods=['GET'])
def profile(isMe):
    auth = current_user.is_authenticated
    if isMe == '1':
        return render_template('profile.html', owner=True, auth=auth)
    else:
        return render_template('profile.html', owner=False, auth=auth)

@APP.route('/orderState')
def order_state():
    auth = current_user.is_authenticated
    return render_template('order-state.html', auth=auth)

@APP.route('/item')
def add_item():
    auth = current_user.is_authenticated
    return render_template('item.html', auth=auth)

@APP.route('/history')
@login_required
def history():
    auth = current_user.is_authenticated
    return render_template('history.html', auth=auth)

@APP.route('/another')
@login_required
def another():
    auth = current_user.is_authenticated
    return render_template('another.html', auth=auth)

@APP.route('/todo')
@login_required
def todo():
    auth = current_user.is_authenticated
    return render_template('todo.html', auth=auth)

@APP.route('/order')
@login_required
def order():
    auth = current_user.is_authenticated
    return render_template('order.html', auth=auth)

if __name__ == '__main__':
    APP.run(debug=True)