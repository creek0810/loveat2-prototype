from flask import Blueprint, render_template, redirect, request
from flask_login import login_required, current_user
from lib.auth import admin_required

menu_web = Blueprint('menu_web', __name__)

@menu_web.route('/', methods=["GET"])
def menu():
    print(current_user.role)
    return render_template('menu.html', auth=current_user.role, name=current_user.id)

@menu_web.route('/edit', methods=["GET"])
@admin_required
def edit():
    return render_template('menu-edit.html', auth=current_user.role, name=current_user.id)

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