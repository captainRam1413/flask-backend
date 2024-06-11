from config import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone_number = db.Column(db.String(10), unique=True,nullable=False)
    pswd=db.relationship('Pswd',uselist=False,back_populates='user')
    ans = db.relationship('Ans',backref='author',lazy=True)
    dashbord=db.relationship('Dashbord',uselist=False,back_populates='user')
    
    
    def to_json(self):
        return {
            'user_id': self.id,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'email': self.email,
            'phoneNumber' : self.phone_number,
            'password':self.pswd.password 
        }
        
    def check_password(self,password):
        return self.password == password
    
    
class Pswd(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'),unique=True)
    password = db.Column(db.Integer,nullable=False)
    pswd=db.relationship('User',uselist=False,back_populates='pswd')
    
    def to_json(self):
        return{
            'id':self.id,
            'user_id':self.user_id,
            'password':self.password
        }
        
        
class Dashbord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'),nullable = False)
    user= db.relationship('User',uselist=False,back_populates='pswd')
    
    def to_json(self):
        return{
            'id':self.id,
            'user_id':self.user_id
        }
    
    


class Que(db.Model):
    que_id = db.Column(db.Integer, primary_key=True)
    que_string = db.Column(db.String(255),nullable=False,unique=True)
    ans = db.relationship('Ans',backref='que',lazy=True)
    
    def to_json(self):
        return{
            'que_id':self.que_id,
            'que_string':self.que_string            
        }
    
    
    
    
class Ans(db.Model):
    ans_id = db.Column(db.Integer, primary_key=True)
    que_id = db.Column(db.Integer, db.ForeignKey('que.que_id'), nullable=False)
    ans_string = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"),nullable=False)
    
    def to_json(self):
        return{
            'ans_id':self.ans_id,
            'que_id':self.que_id,
            'user_id':self.user_id,
            'ans_string':self.ans_string
        }
    
            
        