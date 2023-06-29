from flask import render_template, redirect, url_for, jsonify

from app.main import bp

from app.buckets.bosses import get_boss_list
from app.buckets.spells import get_spell_info
from app.models.warcraftlogs import serialized_spell


@bp.route('/api.healer_cds.com/spells')
def get_api_spells():
    spells = get_spell_info()
    serialized = [serialized_spell(s) for s in spells]
    
    return jsonify(spells=serialized)



@bp.route('/')
def index():
    return redirect('/healers_home')

@bp.route('/healers_home')
def homepage():
    bosses = get_boss_list()
    spells = get_spell_info()
    return render_template('index.html', bosses=bosses, spells=spells)