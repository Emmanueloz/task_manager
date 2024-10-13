from flask_login import LoginManager, UserMixin
from app.features.auth.model import User


login_manager = LoginManager()


class UserLogin(UserMixin):
    def __init__(self, user: User):
        self.id = user.id
        self.username = user.username
        self.email = user.email


login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
