from app.API_queries import url, headers
import requests

    
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