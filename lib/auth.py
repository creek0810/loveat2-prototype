from functools import wraps
from flask_login import LoginManager, UserMixin, current_user, AnonymousUserMixin

from models import user
class Anonymous(AnonymousUserMixin):
    def __init__(self):
        self.role = 'anonymous'
        self.id = 'anonymous'
    def get_role(self):
        return self.role

class User(UserMixin):
    def get_role(self):
        return self.role

login_manager = LoginManager()
login_manager.anonymous_user = Anonymous

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
@login_manager.user_loader
def user_loader(id):
    target = {}
    for i in test_data:
        if i["id"] == id:
            tmpUser= User()
            tmpUser.id = i["id"]
            tmpUser.role = i["role"]
            return tmpUser
    return None

def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if current_user.is_authenticated and current_user.role == "admin":
            return f(*args, **kwargs)
        else:
            return login_manager.unauthorized()
    return wrap