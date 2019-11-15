from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from lib.auth import admin_required

another_web = Blueprint('another_web', __name__)

@another_web.route('/', methods=["GET"])
def home():
    return redirect(url_for('menu_web.menu'))

@another_web.route('/cart', methods=["GET"])
def cart():
    return render_template('cart.html', auth=current_user.role, name=current_user.id)

@another_web.route('/business_time', methods=["GET"])
def business_time():
    return "hello"
