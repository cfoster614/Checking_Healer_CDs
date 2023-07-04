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
                    id
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
    
