from app.models.warcraftlogs import run_query
from app.buckets.bosses import get_boss_list

def url_to_log_code(url, boss):
    code= url.split("/")[-1]
    data = report_data(code, boss)
    return data

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
    
def get_boss_info(id):
    bosses = get_boss_list()
    for boss in bosses:
        if boss.id == id:
            return boss