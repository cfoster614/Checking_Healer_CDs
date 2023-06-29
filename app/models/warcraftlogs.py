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
    
    
     
        
class Spell:
    """Major healing cooldown spells."""
    
    def __init__(self, id, name, icon):
        self.id = id
        self.name = name
        self.icon = icon
        
    def __repr__(self):
        return f"<id={self.id}, name={self.name}, icon={self.icon}>"
    
    
def serialized_spell(self):
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