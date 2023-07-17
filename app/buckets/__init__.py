from flask import Blueprint

bp = Blueprint('buckets', __name__)

from app.buckets import bosses, report, spells
