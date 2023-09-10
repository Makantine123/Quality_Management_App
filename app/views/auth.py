"""Module contains authorization routes"""

from flask_login import login_user, login_required, logout_user
from werkzeug import test
from werkzeug.security import generate_password_hash, check_password_hash
from flask import app, flash, redirect, render_template, request, url_for
from sqlalchemy.util import method_is_overridden
from models import storage
from models.user import User
from views import app_views
from views import dash_views


@app_views.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""
    return render_template('auth/login.html')


@app_views.route('/register', methods=['GET', 'POST'])
def register():
    """Register page"""
    return render_template('/auth/register.html')


@app_views.route('/signup', methods=['POST'])
def signup():
    """Singup route method"""
    submitted_form = request.form
    fusername = submitted_form.get('username')
    femail = submitted_form.get('email')
    fpassword = submitted_form.get('password')
    if (fusername is not None and
        femail is not None and
            fpassword is not None):

        currentuser = storage.query_db(User).filter_by(username=fusername).first()

        if currentuser:
            flash('Username already exists', 'user_error')
            return redirect(url_for('app_views.register'))

        currentemail = storage.query_db(User).filter_by(email=femail).first()
        if currentemail:
            flash('Email already exists', 'email_error')
            return redirect(url_for('app_views.register'))
        new_user = User()
        new_user.username = fusername
        new_user.password_hsh = generate_password_hash(fpassword, method='sha256')
        new_user.email = femail
        storage.new(new_user)
        storage.save()
        flash('User successfully registered. Please login')
        return redirect(url_for('app_views.login'))
    return render_template('index.html')


@app_views.route('/signing_in', methods=['GET', 'POST'])
def signing_in():
    """Signing in route"""
    submitted_form = request.form
    femail = submitted_form.get('email')
    fpassword = submitted_form.get('password')

    curruser = storage.query_db(User).filter_by(email=femail).first()
    if not curruser or not check_password_hash(curruser.password_hsh, fpassword):
        flash('Error! Login details incorrect.Please check your details and try again.')
        return redirect(url_for('app_views.login'))

    login_user(curruser)
    return redirect(url_for('dash_views.home'))


@app_views.route('/log_out', methods=['GET', 'POST'])
@login_required
def log_out():
    """Logout User"""
    logout_user()
    return redirect(url_for('app_views.login'))
