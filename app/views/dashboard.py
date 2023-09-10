"""Module contains Dashboard"""
from flask import Blueprint
from flask import app, flash, redirect, render_template, request, url_for
from flask_login import login_required
from sqlalchemy.util import method_is_overridden
from models import storage
from models.user import User
from views import dash_views


@dash_views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    """Dash board route"""
    return render_template('quality_control/home.html')
