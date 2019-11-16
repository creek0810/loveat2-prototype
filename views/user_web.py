from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user, logout_user
from lib.auth import admin_required, login_manager

user_web = Blueprint('user_web', __name__)

@user_web.route('/logout', methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for('menu_web.menu'))


@user_web.route('/forgetpassword', methods=["GET"])
def forgetpassword():
    return render_template('forget-password.html', auth=current_user.role, name=current_user.id)


@user_web.route('/profile/<id>', methods=['GET'])
@login_required
def profile(id):
    user_id = current_user.id
    print(user_id, id)
    if id == user_id:
        print("owner")
        return render_template('profile.html', owner=True, auth=current_user.role, name=user_id)
    elif current_user.role == "admin":
        return render_template('profile.html', owner=False, auth=current_user.role, name=user_id)
    else:
        return login_manager.unauthorized()
