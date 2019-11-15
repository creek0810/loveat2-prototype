from flask import Blueprint, render_template
from flask_login import login_required, current_user
from lib.auth import admin_required

order_web = Blueprint('order_web', __name__)

@order_web.route('/history', methods=["GET"])
@admin_required
def history():
    return render_template('history.html', auth=current_user.role, name=current_user.id)

@order_web.route('/todo', methods=["GET"])
@admin_required
def todo():
    return render_template('todo.html', auth=current_user.role, name=current_user.id)

@order_web.route('reply', methods=['GET'])
@admin_required
def reply():
    auth = current_user.is_authenticated
    return render_template('order.html', auth=current_user.role, name=current_user.id)

@order_web.route('state', methods=["GET"])
@login_required
def state():
    return render_template('order-state.html', auth=current_user.role, name=current_user.id)
