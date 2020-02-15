from app import db


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), index=True, unique=False)

    def __repr__(self):
    	return '<User %r>' % (self.description)
