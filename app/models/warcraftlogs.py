from flask import request
from app.models.logs_database import Spell
import requests
import os
token = os.environ.get('API_TOKEN')

def serialized(self):
    return {
        "id": self.id,
        "name": self.name,
        "icon": self.icon
    }
    

def serialized_spell(self):
    return {
        "spell_id": self.spell_id,
        "name": self.name,
        "icon": self.icon
    }
    

def run_query(query):
    """Helper function for queries."""
    headers = {
    'Authorization' : f'Bearer {token}'
    }
    
    url = "https://www.warcraftlogs.com/api/v2/client"
    
    data = {
        'query' : query
    }
    response = requests.get(url, headers=headers, json=data)
    data = response.json()
    
    return data
           
                 
def readable_time(time):
    """ Timestamps are in milliseconds.
        Need to convert properly to minutes/seconds.
        
        >>> readable_time(35822)
        '00:35'
    """
    m_sec = time
    seconds = m_sec // 1000
    minutes = seconds // 60
    rem_sec = seconds % 60
    formatted_time = f"{minutes:02d}:{rem_sec:02d}"
    
    return formatted_time

def filter_spells(players):
    spell_list = []
    for spell in players:
        print(spell)
        spell_list.append(spell['name'])
    return spell_list

def get_spell_times_from_form(players):
    spell_info_list = []
    seen_combination = set()
    
    for player in players:
        spells = request.form.getlist(f'spells {player}')
        for spell in spells:
            combination = (player, spell)
         
            if combination not in seen_combination:
                times = request.form.getlist(f'{spell} {player} timers')
                seen_combination.add(combination)

                spell_info = Spell.query.filter_by(name=spell).first()
                spell_info_dict = {
                    'name': spell,
                    'times': times,
                    'icon': f'{spell_info.icon}',
                    'player_name': player
                }
                spell_info_list.append(spell_info_dict)
    
    return spell_info_list

