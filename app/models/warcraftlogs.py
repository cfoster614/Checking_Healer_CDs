from app.API_queries import url, headers
import requests


class Boss:
    """Bosses for Aberrus."""
    
    def __init__(self, id, name, icon):
        self.id = id
        self.name = name
        self.icon = icon
    def __repr__(self):
        return f"<id={self.id}, name={self.name}, icon={self.icon}>"
    
    @property
    def boss_id(self):
        return self.id
    
    
     
        
class Spell:
    """Major healing cooldown spells."""
    
    def __init__(self, id, name, icon):
        self.id = id
        self.name = name
        self.icon = icon
        
    def __repr__(self):
        return f"<id={self.id}, name={self.name}, icon={self.icon}>"
    
    
def serialized(self):
    return {
        "id": self.id,
        "name": self.name,
        "icon": self.icon
    }

    
class Query:
    """For an easier time running queries to the API."""
    def __init__(self, query):
        self.query = query
        
    def run_query(self):
        data = {
            'query' : self.query
        }
        response = requests.get(url, headers=headers, json=data)
        data = response.json()
        
        return data

def run_query(query):
        data = {
            'query' : query
        }
        response = requests.get(url, headers=headers, json=data)
        data = response.json()
        
        return data
    
class Report_encounters:
    
    def __init__(self, id, boss_id, fight_percentage, difficulty):
        self.id = id,
        self.boss_id = boss_id,
        self.fight_percentage = fight_percentage,
        self.difficulty = difficulty
        
