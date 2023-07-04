from flask import render_template, redirect, url_for, jsonify, request, current_app

from app.main import bp

from app.buckets.bosses import add_bosses_to_database
from app.buckets.spells import add_to_database
from app.buckets.report import url_to_log_code, report_data
from app.models.warcraftlogs import serialized
from app.models.logs_database import Spell, Boss, seed_database


@bp.route('/api.healer_cds.com/spells')
def get_api_spells():
    spells = Spell.query.all()
    serialized_spells = [serialized(s) for s in spells]
    
    return jsonify(spells=serialized_spells)


@bp.route('/api.healer_cds.com/bosses')
def get_api_bosses():
    bosses = Boss.query.all()
    serialized_bosses = [serialized(s) for s in bosses]
    
    return jsonify(bosses=serialized_bosses)
    
@bp.route('/populate_database')
def populate_database():
    """Updates the database within app context."""
    with current_app.app_context():
        seed_database()
        spells = add_to_database()
        bosses = add_bosses_to_database()
    return redirect('/healers_home')



@bp.route('/')
def index():
    return redirect('/healers_home')


@bp.route('/healers_home', methods=['GET', 'POST'])
def homepage():
    """Selection of bosses to choose."""
    if request.method == 'GET':
        bosses = Boss.query.all()
        return render_template('index.html', bosses=bosses)
    
    if request.method == 'POST':
        report_url = request.form.get('log-input')
        boss = request.form.get('boss-list')
        code = url_to_log_code(report_url)
      
        return redirect(url_for('main.show_results', code = code, bossID = boss))


@bp.route('/healers_home/report?boss=<int:bossID>&lr=<code>', methods=['POST', 'GET'])
def show_results(bossID, code):
        encounter = report_data(code, bossID)
        boss_info = Boss.query.filter_by(boss_id = bossID).first()
    
        return render_template('results.html', ecounter = encounter, boss = boss_info)