from app.models.warcraftlogs import run_query, readable_time
from app.models.logs_database import Spell
import re

def url_to_log_code(url):
    """Split the url the user submitted to just the code for API query.

        >>> url_to_log_code('https://www.warcraftlogs.com/reports/btCAvx2fPwRgNy8F')
        'btCAvx2fPwRgNy8F'
        
        >>> url_to_log_code('https://www.warcraftlogs.com/reports/nJKY8FbrVW4cyDLC#fight=last&type=healing')
        'nJKY8FbrVW4cyDLC'
    """
    
    pattern = fr"(?<=/reports/)([^/#]{{16,}})"
    match = re.search(pattern, url)
    if match:
        code = match.group(1)
    else:
        code = None
    return code


def report_data(code, boss):
    """
    All the info we need for report html page.
    Just need the report code and the encounterID.
    Gives list of all wipes/kills from that boss.
    """
    query = f'''
        query reportData {{
            reportData {{report(code: "{code}"){{
                fights(killType: Encounters, encounterID: {boss}) {{
                    encounterID, 
                    difficulty, 
                    fightPercentage, 
                    id,
                    endTime,
                    startTime,
                    kill
                }}
            }}
        }}
    }}
    '''
    results = run_query(query)
    
    try:
        encounters= results['data']['reportData']['report']['fights']
        
    except (KeyError) as e:
        print(f"Error accessing response data: {e}")
        
    return encounters


def serialized_encounter(self):
    return {
        "id": self.id,
        "boss_id" : self.boss_id,
        "fight_percentage" : self.fight_percentage,
        "difficulty": self.difficulty
    }
    

def fight_data(code, fightID):
    #Get fight data again for endTime and startTime.
    query = f''' 
        query reportData {{
            reportData {{report(code: "{code}"){{
                fights(killType: Encounters, fightIDs: {fightID}) {{
                    endTime,
                    startTime
                }}
            }}
        }}
    }}
    '''
    results = run_query(query)
    timers = results['data']['reportData']['report']['fights']
    
    for time in timers:  
        start_time = (time['startTime'])
        duration = time['endTime'] - time['startTime']
        d_time = readable_time(duration)
        time_dict = {'start' : start_time,
                     'duration' : duration,
                     'd_time' : d_time}
       
        return time_dict
    
            
def correct_spell(spell_list, code, fightID, fight_info):
    """
    Query report using the spells given and the fightID. 
    This gives us all the spell data/player data we need.
    """
    
    spells_list = [Spell.query.filter_by(name = spell_name).all() for spell_name in spell_list] #Take spell list and make new list with spell ids for query.
        
    spell_data = []
    for spell in spells_list: #Run a query for every spell given. 
        for s in spell:
            query = f'''
                query reportData {{ 
                    reportData {{report(code: "{code}") {{
                        graph(dataType: Casts, fightIDs: {fightID}, abilityID: {s.spell_id})
                    }}
                }}
            }}
            '''
            results = run_query(query)  
            spell_info = results['data']['reportData']['report']['graph']['data']['series']
            simplified_data = [] #Data comes out with more than we need. Makes it difficult to sort through.
            
            if not spell_info:
                #We want to show the user if a spell they assigned wasn't used that pull.
                ability = "Not used"
                simplified_data.append({'spell' : s.name, 'ability' : ability})
                
            for player_data in spell_info:
                #Simplify the data to an easier format for flask template, only info we need.
                name = player_data['name']
                abilities = []

                for event in player_data['events']:
                    for e in event:
                        if 'timestamp' in e and 'ability' in e and 'name' in e['ability'] and 'abilityIcon' in e['ability']:
                            ability_data = [e['ability']['name'], e['timestamp'] - fight_info['start'], e['ability']['abilityIcon'], e['type']]
                            abilities.append(ability_data)
                    simplified_data.append({'name': name, 'abilities': abilities})
            spell_data.append(simplified_data)
            
    return spell_data
            


                
