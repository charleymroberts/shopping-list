from app import app, db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=False)

    def __repr__(self):
        return f"{self.name}"
