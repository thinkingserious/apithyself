from .. import db

class HealthGoal(db.Model):
    __tablename__ = 'health_goal'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10))
    weight = db.Column(db.Integer)

class HealthWeight(db.Model):
    __tablename__ = 'health_weight'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10))
    weight = db.Column(db.Integer)

class HealthCalories(db.Model):
    __tablename__ = 'health_calories'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10))
    calories = db.Column(db.Integer)
