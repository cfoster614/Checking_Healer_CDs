from flask import render_template, redirect, url_for, jsonify, request

from app.main import bp

from app.buckets.bosses import get_boss_list, boss_ids
from app.buckets.spells import get_spell_info
from app.buckets.report import url_to_log_code, report_data, get_boss_info
from app.models.warcraftlogs import serialized


@bp.route('/api.healer_cds.com/spells')
def get_api_spells():
    spells = get_spell_info()
    serialized_spells = [serialized(s) for s in spells]
    
    return jsonify(spells=serialized_spells)

@bp.route('/api.healer_cds.com/bosses')
def get_api_bosses():
    bosses = get_boss_list()
    serialized_bosses = [serialized(s) for s in bosses]
    
    return jsonify(bosses=serialized_bosses)
    



@bp.route('/')
def index():
    return redirect('/healers_home')

@bp.route('/healers_home', methods=['GET'])
def homepage():
    bosses = get_boss_list()
    spells = get_spell_info()
    return render_template('index.html', bosses=bosses, spells=spells)


@bp.route('/healers/results', methods=['POST', 'GET'])
def show_results():
    
    report_url = request.form.get('log-input')
    boss = request.form.get('boss-list')
    
    boss_id = int(boss)
    
    encounter = url_to_log_code(report_url, boss_id)
    boss_info = get_boss_info(boss_id)
    
   
   
    
    
    return render_template('results.html', encounter = encounter, boss = boss_info)