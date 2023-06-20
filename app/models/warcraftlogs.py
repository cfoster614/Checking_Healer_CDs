class Boss:
    """Bosses for Aberrus."""
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __repr__(self):
        return f"<id={self.id}, name={self.name}>"
        
class Spell:
    """Major healing cooldown spells."""
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __repr__(self):
        return f"<id={self.id}, name={self.name}>"