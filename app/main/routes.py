from flask import render_template, redirect, url_for, jsonify, request, session, flash, get_flashed_messages
from app.main import bp
from app.extensions import db
import json
from app.buckets.bosses import populate_bosses
from app.buckets.spells import populate_spells
from app.buckets.report import url_to_log_code, report_data, fight_data, correct_spell
from app.models.warcraftlogs import serialized, serialized_spell, readable_time, get_spell_times_from_form, filter_spells
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
    bosses = Boss.query.all()
    path = request.path #For navbar
   
    if request.method == 'POST':
        report_url = request.form.get('log-input')
        code = url_to_log_code(report_url)
        boss_input = request.form.get('boss-list') 
        boss_info = Boss.query.filter_by(boss_id=boss_input).first()
        boss_id = boss_info.boss_id
        
        if code:
            return redirect(url_for('main.show_results', code = code, bossID = boss_id))
            
        else:
            #Need a valid url to continue or the api query would break.
            flash("Invalid log url.")
         
    return render_template('index.html', bosses=bosses, path=path)


@bp.route('/healers_home/report<int:bossID>_<code>', methods=['POST', 'GET'])
def show_results(bossID, code):
    """Show boss selected and all the pulls in the encounter. 
        Spell and timer inputs.
    """
     #Query warcraftlogs for encounter info pulls.
    boss_info = Boss.query.filter_by(boss_id=bossID).first()
    path = request.path
    result_data = report_data(code, bossID)
    
    if result_data['encounters']:
                session['log_title'] = result_data['log_title']
                session['guild'] = result_data['guild']
    else:
        #If the boss isn't in the report, return error to stop app breaking after spell input.
        #Redirect to homepage to select a new boss.
        flash("Looks like you didn't do that boss. Select a different one!")
        return redirect('/healers_home')
   
    
    if request.method == 'GET':
        assignment_data = session.get('assignment_data', None)
        log_title = result_data['log_title']
        guild = result_data['guild']
        
            
        return render_template('results.html', boss=boss_info, readable_time=readable_time, path=path, code=code, assignment_data=assignment_data, encounter=result_data['encounters'], guild=guild, log_title=log_title)

    if request.method == 'POST':
        pullID = request.form.get('pull-list')
        players = request.form.getlist('player-name')

        assignment_data = get_spell_times_from_form(players)  #We want the spells to be together with appropriate times.
        session['assignment_data'] = assignment_data
        
        spell_names = filter_spells(assignment_data) #Get spell names from form and check if it's in the database.
        print(spell_names)
        session['spell_names'] = spell_names

        return redirect(url_for('main.comparison', pullID=pullID, bossID=bossID, code=code))

        
@bp.route('/healers_home/report<int:bossID>_<code>/comparison<int:pullID>', methods=['POST', 'GET'])
def comparison(pullID,  code, bossID):
    assignment_data = session.get('assignment_data', [])
    spell_names = session.get('spell_names', [])
    log_title = session.get('log_title', [])
    guild = session.get('guild', [])
    path = request.path
    print('assignemnt', assignment_data)
    
    fight_info = fight_data(code, pullID) #Start and end times of encounter.
    duration = fight_info['duration'] #Needed for converting the time the player cast the spell to a readable format.
    seconds = duration // 1000 #Needed for creating spell timeline div, slightly different from just the duration time.
   
    report_data = correct_spell(spell_names, code, pullID, fight_info) #Main function for getting info like players, casts, cast times, spells, etc.
  
    return render_template('comparison.html', events = report_data, duration = duration, readable_time = readable_time, seconds=seconds, path=path, boss=bossID, code=code, assignment_data=assignment_data, guild=guild, log_title=log_title)
      