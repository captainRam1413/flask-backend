from config import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone_number = db.Column(db.String(10), unique=True, nullable=False)
    is_ans_given = db.Column(db.Boolean, default=False)
    # One-to-one relationship
    pswd = db.relationship('Pswd', uselist=False, back_populates='user', cascade="all, delete-orphan")
    
    # One-to-many relationship
    ans = db.relationship('Ans', backref='author', lazy=True, cascade="all, delete-orphan")
    
    # One-to-many relationship
    userans = db.relationship('Userans', backref='author', lazy=True, cascade="all, delete-orphan")
    
    # One-to-one relationship
    dashboard = db.relationship('Dashboard', uselist=False, back_populates='user', cascade="all, delete-orphan")

    def to_json(self):
        return {
            'user_id': self.user_id,  # corrected from self.id
            'firstName': self.first_name,
            'lastName': self.last_name,
            'email': self.email,
            'phoneNumber': self.phone_number,
            'password': self.pswd.password if self.pswd else None,
            'isAnsGiven': self.is_ans_given
        }
        
    def check_password(self, password):
        return self.pswd.password == password if self.pswd else False  # corrected the logic
    
    
class Pswd(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), unique=True)
    password = db.Column(db.String(255), nullable=False)  # use String for hashed password
    user = db.relationship('User', back_populates='pswd')  # corrected relationship
    
    def to_json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'password': self.password
        }
        
        
class Dashboard(db.Model):  # corrected class name to 'Dashboard'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    user = db.relationship('User', back_populates='dashboard')  # corrected relationship
    
    
class Que(db.Model):
    que_id = db.Column(db.Integer, primary_key=True)
    que_string = db.Column(db.String(255), nullable=False, unique=True)
    que_type = db.Column(db.String(255),nullable=False)
    startup_stage = db.Column(db.String(255),nullable=False)
    ans = db.relationship('Ans', backref='que', lazy=True, cascade="all, delete-orphan")
    
    
    def to_json(self):
        return{
            'question_id': self.que_id,
            'que_string': self.que_string,
            'que_type':self.que_type,
            'startup_stage':self.startup_stage
            
        }
        
class Ans(db.Model):
    ans_id = db.Column(db.Integer, primary_key=True)
    que_id = db.Column(db.Integer, db.ForeignKey('que.que_id'), nullable=False)
    ans_string = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    
    
    def to_json(self):
        return{
            'ans_id': self.ans_id,
            'id': self.que_id,
            'ans': self.ans_string,
            'user_id': self.user_id
        }
        
class Userque(db.Model):
    que_id = db.Column(db.Integer, primary_key=True)
    que_string = db.Column(db.String(255), nullable=False, unique=True)
    que_type = db.Column(db.String(255),nullable=False)
    
    userans = db.relationship('Userans', backref='userque', lazy=True, cascade="all, delete-orphan")
    
    
    def to_json(self):
        return{
            'question_id': self.que_id,
            'que_string': self.que_string,
            'que_type':self.que_type,
            
            
        }
        
class Userans(db.Model):
    ans_id = db.Column(db.Integer, primary_key=True)
    que_id = db.Column(db.Integer, db.ForeignKey('userque.que_id'), nullable=False)
    ans_string = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    
    
    def to_json(self):
        return{
            'user_ans_id': self.ans_id,
            'id': self.que_id,
            'ans': self.ans_string,
            'user_id': self.user_id
        }