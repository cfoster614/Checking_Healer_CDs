from flask import render_template, redirect, url_for, jsonify, request, current_app
from jinja2 import Template
from app.main import bp
from app.extensions import db

from app.buckets.bosses import populate_bosses
from app.buckets.spells import populate_spells
from app.buckets.report import url_to_log_code, report_data, fight_data, correct_spell
from app.models.warcraftlogs import serialized, serialized_spell, readable_time
from app.models.logs_database import Spell, Boss



@bp.route('/api.healer_cds.com/spells')
def get_api_spells():
    spells = Spell.query.all()
    serialized_spells = [serialized_spell(s) for s in spells]
    
    return jsonify(spells=serialized_spells)


@bp.route('/api.healer_cds.com/bosses')
def get_api_bosses():
    bosses = Boss.query.all()
    serialized_bosses = [serialized(s) for s in bosses]
    
    return jsonify(bosses=serialized_bosses)
    
@bp.route('/populate_database')
def populate_database():
    """Updates the database within app context."""
    db.drop_all()
    db.create_all()
    
    populate_bosses()
    populate_spells()
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
    
    if request.method == 'GET':
        encounter = report_data(code, bossID)
        boss_info = Boss.query.filter_by(boss_id = bossID).first()
    
        return render_template('results.html', encounter = encounter, boss = boss_info, readable_time = readable_time)
    
    if request.method == 'POST':
        pullID = request.form.get('pull-list')
        spells = request.form.getlist('hidden-ids')
        timers = request.form.getlist('timers')
       
        return redirect(url_for('main.comparison', pullID = pullID, bossID = bossID, code = code, spells = spells))
    
    
@bp.route('/healers_home/report?boss=<int:bossID>&lr=<code>/comparison?encounter=<int:pullID>', methods=['POST', 'GET'])
def comparison(pullID,  code, bossID):
    input_values = request.args.getlist('spells')
    fight_info = fight_data(code, pullID)
    duration = fight_info['duration']
    seconds = duration // 1000
    print(duration, seconds)
  
    
    spell_info = correct_spell(input_values, code, pullID, fight_info)
    
    
    return render_template('comparison.html', events = spell_info, duration = duration, readable_time = readable_time, seconds=seconds)
      