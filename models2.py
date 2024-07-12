from datetime import datetime

from config import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone_number = db.Column(db.String(10), unique=True, nullable=False)
    is_ans_given = db.Column(db.Boolean, default=False)
    current_startup_stage = db.Column(db.Integer,default=1)
    
    # One-to-one relationship
    pswd = db.relationship('Pswd', uselist=False, back_populates='user', cascade="all, delete-orphan")
    
    # One-to-many relationship
    ans = db.relationship('Ans', backref='author', lazy=True, cascade="all, delete-orphan")
    
    # One-to-many relationship
    userans = db.relationship('Userans', backref='author', lazy=True, cascade="all, delete-orphan")
    
    # One-to-one relationship
    dashboard = db.relationship('Dashboard', uselist=False, back_populates='user', cascade="all, delete-orphan")
    
    # Define the many-to-many relationship with Consultant
    consultant = db.relationship('Consultant', secondary='contousers', back_populates='user')

    #
    payment = db.relationship("Payment", backref='author',lazy=True)

    def to_json(self):
        return {
            'user_id': self.user_id,  # corrected from self.id
            'firstName': self.first_name,
            'lastName': self.last_name,
            'email': self.email,
            'phoneNumber': self.phone_number,
            'password': self.pswd.password if self.pswd else None,
            'isAnsGiven': self.is_ans_given,
            'current_startup_stage':self.current_startup_stage
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
            'que_type':self.que_type
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
        
        
        
class Plan(db.Model):
    plan_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    
    def to_json(self):
        return {
            'plan_id': self.plan_id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }


class Payment(db.Model):
    payment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    transaction_id = db.Column(db.String(255), nullable=False, unique=True)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.plan_id'), nullable=False)
    
    user = db.relationship('User', back_populates='payment', overlaps="author")
    plan = db.relationship('Plan')
    
    def to_json(self):
        return {
            'payment_id': self.payment_id,
            'user_id': self.user_id,
            'amount': self.amount,
            'date': self.date,
            'status': self.status,
            'transaction_id': self.transaction_id,
            'plan_id': self.plan_id,
            'plan': self.plan.to_json()
        }
      
        


class Consultant(db.Model):
    __tablename__ = 'consultant'
    
    consultant_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=False, unique=True)
    consulting_field = db.Column(db.String(100), nullable=False)
    experience_years = db.Column(db.Integer, nullable=False)
    
    # Many-to-many relationship with User
    user = db.relationship('User', secondary='contousers', back_populates='consultant')
    
    con_pswd = db.relationship("ConPswd", uselist=False, back_populates='consultant', cascade="all, delete-orphan")  # corrected relationship

    def to_json(self):
        return {
            'consultant_id': self.consultant_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'consulting_field': self.consulting_field,
            'experience_years': self.experience_years,
        }
        

class ConPswd(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    consultant_id = db.Column(db.Integer, db.ForeignKey('consultant.consultant_id'), unique=True)
    pswd = db.Column(db.String(255), nullable=False)  # use String for hashed password
    consultant = db.relationship('Consultant', back_populates='con_pswd')  # corrected relationship
    
    def to_json(self):
        return {
            'id': self.id,
            'consultant_id': self.consultant_id,
            'password': self.pswd
        }
 
        
class ConToUser(db.Model):
    __tablename__ = 'contousers'
    
    id = db.Column(db.Integer, primary_key=True)
    consultant_id = db.Column(db.Integer,db.ForeignKey('consultant.consultant_id'), nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'), nullable=False)
    
    def to_json(self):
        return {
            'id': self.id,
            'consultant_id': self.consultant_id,
            'user_id': self.user_id,
        }