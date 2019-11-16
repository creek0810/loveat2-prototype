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

@menu_web.route('/add/item', methods=["GET"])
@admin_required
def add_item():
    return render_template('edit-add-item.html', auth=current_user.role, name=current_user.id, add=True)

@menu_web.route('/add/combo', methods=["GET"])
@admin_required
def add_combo():
    return render_template('edit-add-combo.html', auth=current_user.role, name=current_user.id, add=True)

@menu_web.route('/edit/item', methods=["GET"])
@admin_required
def edit_item():
    return render_template('edit-add-item.html', auth=current_user.role, name=current_user.id, add=False)

@menu_web.route('/edit/combo', methods=["GET"])
@admin_required
def edit_combo():
    return render_template('edit-add-combo.html', auth=current_user.role, name=current_user.id, add=False)