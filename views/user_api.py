from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import current_user, login_user
from lib.auth import User

user_api = Blueprint('user_api', __name__)

test_data = [
    {
        "id": "admin",
        "role": "admin",
    },
    {
        "id": "customer",
        "role": "customer",
    }
]
@user_api.route('/login', methods=['POST'])
def login():
    id = request.form["user-name"]
    target = {}
    for i in test_data:
        if i["id"] == id:
            tmpUser = User()
            tmpUser.id = i["id"]
            tmpUser.role = i["role"]
            login_user(tmpUser)
            break
    return redirect(url_for('menu_web.menu'))

@user_api.route('/register')
def register():
    pass

"""
@APP.route('/login', methods=['GET'])
def login():
    tmp= User()
    tmp.id = "admin"
    tmp.role = "admin"
    login_user(tmp)
    return redirect(url_for('menu'))
 
@APP.route('/login2', methods=['GET'])
def logi2n():
    tmp= User()
    tmp.id = "customer"
    tmp.role = "customer"
    login_user(tmp)
    return redirect(url_for('menu'))

@APP.route('/')
def menu():
    tmp = current_user.get_role()
    return render_template('menu.html', auth=tmp, name="river")


@APP.route('/test_admin')
@admin_required
def test_admin():
    return "this is admin"

@APP.route('/test_auth')
@login_required
def test_auth():
    return "this is auth
"""