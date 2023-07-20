from flask import render_template, redirect, url_for, jsonify, request
from app.main import bp
from app.extensions import db
import json
from app.buckets.bosses import populate_bosses
from app.buckets.spells import populate_spells
from app.buckets.report import url_to_log_code, report_data, fight_data, correct_spell
from app.models.warcraftlogs import serialized, serialized_spell, readable_time
from app.models.logs_database import Spell, Boss

@bp.route('/api.healer_cds.com/spells')
def get_api_spells():
    """Api for frontend to access spells."""
    spells = Spell.query.all()
    serialized_spells = [serialized_spell(s) for s in spells]
    
    return jsonify(spells=serialized_spells)


@bp.route('/api.healer_cds.com/bosses')
def get_api_bosses():
    """Api for frontend to access bosses."""
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
    """Selection of bosses to choose and report url."""
    error = request.args.get('error')
    bosses = Boss.query.all()
    path = request.path #For navbar
   
    if request.method == 'POST':
        report_url = request.form.get('log-input')
        boss = request.form.get('boss-list')
        code = url_to_log_code(report_url)
        if code:
            return redirect(url_for('main.show_results', code = code, bossID = boss))
        else:
            #Need a valid url to continue or the api query would break.
            error = "Invalid log url."
            
    return render_template('index.html', bosses=bosses, path=path, error=error)


@bp.route('/healers_home/report<int:bossID><code>', methods=['POST', 'GET'])
def show_results(bossID, code):
    """Show boss selected and all the pulls in the encounter. 
        Spell and timer inputs.
    """
    encounter = report_data(code, bossID) #Query warcraftlogs for encounter info pulls.
    boss_info = Boss.query.filter_by(boss_id=bossID).first()
    path = request.path

    if not encounter:
        #If the boss isn't in the report, return error to stop app breaking after spell input.
        #Redirect to homepage to select a new boss.
        error = "Looks like you didn't do that boss. Select a different one!"
        return redirect(url_for('main.homepage', error=error))

    if request.method == 'GET':
        return render_template('results.html', encounter=encounter, boss=boss_info, readable_time=readable_time, path=path, code=code)

    if request.method == 'POST':
        pullID = request.form.get('pull-list')
        spell_names = [spell for spell in request.form.getlist('spells') if spell.strip() and Spell.query.filter_by(name=spell).first()] #Get spell names from form and check if it's in the database.
        
        if not spell_names:
            #We want at least one spell inserted or the query will break.
            error = "Please insert at least one spell."
            return render_template('results.html', encounter=encounter, boss=boss_info, readable_time=readable_time, path=path, code=code, error=error)

        spell_times = []
        for spell in spell_names: #TODO: Turn into a small function elsewhere to shorten code here.
            #The timers and spell inputs need to be separated together, or else it would be confusing.
            #A list of all the timers input without the spells attached would be useless info.
            times = request.form.getlist(f'{spell}-timers')
            spell_info = Spell.query.filter_by(name=spell).first()

            time_obj = {'name': spell,
                        'times': times,
                        'icon': f'{spell_info.icon}'}
            spell_times.append(time_obj)

        timers_json = json.dumps(spell_times) #For passing through as query string.

        return redirect(url_for('main.comparison', pullID=pullID, bossID=bossID, code=code, spells=spell_names, timers=timers_json))

        
@bp.route('/healers_home/report/<int:bossID><code>/comparison<int:pullID>', methods=['POST', 'GET'])
def comparison(pullID,  code, bossID):
    input_values = request.args.getlist('spells')
    path = request.path
    timers_json = request.args.get('timers')
    timers = json.loads(timers_json)
    fight_info = fight_data(code, pullID) #Start and end times of encounter.
    duration = fight_info['duration'] #Needed for converting the time the player cast the spell to a readable format.
    seconds = duration // 1000 #Needed for creating spell timeline div, slightly different from just the duration time.
   
    spell_info = correct_spell(input_values, code, pullID, fight_info) #Main function for getting info like players, casts, cast times, spells, etc.
   
    return render_template('comparison.html', events = spell_info, duration = duration, readable_time = readable_time, seconds=seconds, timers=timers, path=path, boss=bossID, code=code)
      