from app.extensions import db


class Spell(db.Model):
    
    __tablename__ = 'spells'
    id = db.Column(db.Integer, primary_key=True)
    spell_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    icon = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f'<Spell  "{self.name}">'
    
    @classmethod
    def add_spell(cls, **kw):
            obj = cls(**kw)
            db.session.add(obj)
            db.session.commit()

    
class Boss(db.Model):
    
    __tablename__ = 'bosses'
    
    id = db.Column(db.Integer, primary_key=True)
    boss_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    nickname = db.Column(db.String(15))
    icon = db.Column(db.Text, nullable=False)
    
    @classmethod
    def add_boss(cls, **kw):
            obj = cls(**kw)
            db.session.add(obj)
            db.session.commit()
    
    