from exts import db
from datetime import datetime

"""Journal
    journal_id : int (used to identify it by id) primary_key
    date : Date (date added)
    title : String (title of journal)
    description : Text (description, content)

    username : str (to which user this belongs to)
"""
class Journal(db.Model):
    journal_id = db.Column(db.Integer(), primary_key = True)
    date = db.Column(db.Date(), default = datetime.now().strftime("%Y-%m-%d"))
    title = db.Column(db.String(20))
    description = db.Column(db.Text())

    username = db.Column(db.String(30))

    #save 
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    #delete 
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    #update 
    def update(self, title, description):
        self.title = title
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.description = description

""" User
    username: username.
    password : encrypted,
    email: email
"""

class Userdata(db.Model):

    username = db.Column(db.String(30), primary_key = True)
    password = db.Column(db.Text(), nullable = False)
    email = db.Column(db.String(20), nullable = False)


    #save 
    def save(self):
        db.session.add(self)
        db.session.commit()

"""Dates 
"""
class Userdates(db.Model):
    fdlp= db.Column(db.Date(), nullable = False)
    acd = db.Column(db.Integer(), nullable = False)
    next_period_date = db.Column(db.Date())
    fertile_window_start = db.Column(db.Date())
    fertile_window_end = db.Column(db.Date())
    ovulation_date = db.Column(db.Date())
    preg_test_date = db.Column(db.Date())

    username = db.Column(db.String(30), nullable = False)

    usr_id = db.Column(db.Integer(), primary_key = True, nullable = False)

    def __init__(self, username, fdlp, acd, next_period_date, fertile_window_start, fertile_window_end, ovulation_date, preg_test_date):
        self.fdlp = fdlp
        self.acd = acd
        self.next_period_date = next_period_date
        self.fertile_window_start = fertile_window_start
        self.fertile_window_end = fertile_window_end
        self.ovulation_date = ovulation_date
        self.preg_test_date = preg_test_date
        self.username = username

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self,fdlp, acd, next_period_date, fertile_window_start, fertile_window_end, ovulation_date, preg_test_date):
        self.fdlp = fdlp
        self.acd = acd
        self.next_period_date = next_period_date
        self.fertile_window_start = fertile_window_start
        self.fertile_window_end = fertile_window_end
        self.ovulation_date = ovulation_date
        self.preg_test_date = preg_test_date
