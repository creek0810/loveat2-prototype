from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user, logout_user
from lib.auth import admin_required

user_web = Blueprint('user_web', __name__)

@user_web.route('/logout', methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for('menu_web.menu'))

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