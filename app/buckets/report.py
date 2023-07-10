from app.models.warcraftlogs import run_query, Player_Event, readable_time
from app.models.logs_database import Spell


def url_to_log_code(url):
    """
    Split the url the user submitted to just the code for API query.
    Example: 
    """
    code= url.split("/")[-1]
  
    return code

def report_data(code, boss):
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
        
        print(encounters)
        
        
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
    """
    Since we can't query by spell name, and can't be exact with spell_id,
    we have to query our database for a list of spells with the name give by the form data.
    """
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
        s_time = readable_time(start_time)
      
        duration = time['endTime'] - time['startTime']
        d_time = readable_time(duration)
        
        
        time_dict = {'start' : start_time,
                     'duration' : duration,
                     'd_time' : d_time}
       
        return time_dict
        
       
# def correct_spell(spell_list, code, fightID, fight_info):
   
#     spells_list = [Spell.query.filter_by(spell_id = spell_id).all() for spell_id in spell_list]
    
        
#     spell_data = []
#     for spell in spells_list: #Run a query for every spell with the correct name. 
#         for s in spell:
#             print(spell)
#             query = f'''
#                 query reportData {{ 
#                     reportData {{report(code: "{code}") {{
#                         graph(dataType: Casts, fightIDs: {fightID}, abilityID: {s.spell_id})
#                     }}
#                 }}
#             }}
#             '''
#             results = run_query(query)  
#             spell_info = results['data']['reportData']['report']['graph']['data']['series']



#                 #Since cast timestamps are relative to startTimes, we need to subtract from the cast timestamp.
#                 #Convert like usual after the subtraction for cast times.     
#                 # casts = [readable_time(s['timestamp'] - start_time) for s in spell]
#             spell_class= Player_Event(spell_info, fight_info)
#             spell_data.append(spell_class)
        
    
#     return spell_data
            
            
def correct_spell(spell_list, code, fightID, fight_info):
    print(fight_info)
   
    spells_list = [Spell.query.filter_by(spell_id = spell_id).all() for spell_id in spell_list]
    
        
    spell_data = []
    for spell in spells_list: #Run a query for every spell with the correct name. 
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



                #Since cast timestamps are relative to startTimes, we need to subtract from the cast timestamp.
                #Convert like usual after the subtraction for cast times.     
                # casts = [readable_time(s['timestamp'] - start_time) for s in spell]
            simplified_data = []

            for player_data in spell_info:
                
               
                name = player_data['name']
                timestamps = []
                abilities = []

                for event in player_data['events']:
                    for e in event:
                        if 'timestamp' in e and 'ability' in e and 'name' in e['ability'] and 'abilityIcon' in e['ability']:
                            ability_data = [e['ability']['name'], e['timestamp'] - fight_info['start'], e['ability']['abilityIcon'], e['type']]
                            abilities.append(ability_data)

                simplified_data.append({'name': name, 'abilities': abilities})

            spell_data.append(simplified_data)


    return spell_data
            


                
