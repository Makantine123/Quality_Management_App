from flask import Flask, render_template
from flask_login import LoginManager
from flask_cors import CORS
from models.user import User

from models import storage

from views import app_views
from views import dash_views

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/database.db'
app.config['SECRET_KEY'] = 'thisisademo'
app.register_blueprint(app_views)
app.register_blueprint(dash_views)
cors = CORS(app, resources={r"..views/*": {"origins": "*"}})


login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'app_views.login'


@login_manager.user_loader
def load_user(user_id):
    """User loader"""
    return storage.query_db(User).filter_by(id=user_id).first()


@app.teardown_appcontext
def close_db(exception):
    """Closes database session on teardown"""
    storage.close()


@app.route('/')
def home():
    return render_template('auth/login.html')


if __name__ == "__main__":
    app.run(debug=True)
