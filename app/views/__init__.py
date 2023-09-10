from flask import Blueprint

app_views = Blueprint('app_views', __name__)
dash_views = Blueprint('dash_views', __name__)

from views.auth import *
from views.dashboard import *
