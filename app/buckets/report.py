from app.models.warcraftlogs import run_query

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
                    startTime
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
    

def fight_data(spells, code, fightID, name):
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
        start_time = time['startTime']
        duration = time['endTime'] - time['startTime']
        
    fight_length = readable_time(duration) #For later if I want to include the fight duration.
           
    for spell in spells: #Run a query for every spell with the correct name.
        query = f'''
            query reportData {{ 
                reportData {{report(code: "{code}") {{
                    events(dataType: Casts, fightIDs: {fightID}, abilityID: {spell.spell_id}) {{
                        data
                    }}
                }}
            }}
        }}
        '''
        results = run_query(query)
        spell = results['data']['reportData']['report']['events']['data']

        if len(spell) == 0: #If spell results return empty, query again.
            run_query(query)
        else:
            #Since cast timestamps are relative to startTimes, we need to subtract from the cast timestamp.
            #Convert like usual after the subtraction for cast times.     
            # casts = [readable_time(s['timestamp'] - start_time) for s in spell]
            spell_list = []
            for s in spell:
                time = readable_time(s['timestamp'] - start_time)
                spell_info = {'name' : name,
                              'time' : time}
                spell_list.append(spell_info)
               
            print(spell_list)    
            return spell_list
           
            
     
            
def readable_time(time):
    """
    Timestamps are in milliseconds.
    Need to convert properly to minutes/seconds.
    """
    m_sec = time
    seconds = m_sec // 1000
    minutes = seconds // 60
    rem_sec = seconds % 60
    formatted_time = f"{minutes:02d}:{rem_sec:02d}"
    
    return formatted_time
    
      
            
            