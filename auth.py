from flask import Blueprint, jsonify,request
from models2 import User,Pswd,Dashboard,Que,Ans
from config import db
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, create_refresh_token


auth = Blueprint('auth', __name__)

#route for user login
@auth.route('/login-user',methods=['POST'])
def loginuser():
    data=request.get_json()
    email=data.get('email')
    password = data.get('password')
    
    user = User.query.filter_by(email = email).first()
    
    if user and user.pswd.password == password:
        access_token = create_access_token(identity=user.email)
        refresh_token = create_refresh_token(identity=user.email)
        return jsonify(
            {
                'access_token':access_token,
                'email':user.email,
                'refresh_token':refresh_token
            },200
        )
        
#routue for user signup/creating new user
@auth.route('/create-user',methods=['POST'])
def createuser():
    data = request.get_json()
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    password = data.get('password')
    email = data.get('email')
    phonenumber=data.get('phoneNumber')
    
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({
            'message': 'User already exists'
        },403
        )
        
    pswd = Pswd(password = password)
    new_user = User(first_name = first_name,last_name=last_name,email=email,phone_number=phonenumber)
    new_user.pswd = pswd
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:  
        return jsonify({'message':str(e)})
    
    return jsonify(
        {
            'message': 'User created successfully',
        }
    )
    
#route for getting all user imformation    
@auth.route('/getuser')
@jwt_required()
def getuser():
    user = User.query.all()
    json_user = list(map(lambda x: x.to_json(),user))
    return jsonify({"user":json_user})


#route for getting a one user imformation as profile imformation
@auth.route('/getprofile',methods=['GET'])
@jwt_required() 
def getProfile():
    access_token = get_jwt_identity()
    user = User.query.filter_by(email = access_token).first()
    
    return jsonify({"user":user.to_json()})




# route for adding question just for testing
@auth.route('/addQue',methods=['POST'])
@jwt_required()
def addQue():
    data = request.get_json()
    
    que_string = data.get('que_string')
    que_type =data.get('que_type')
    startup_stage = data.get('startup_stage')
    que = Que(que_string = que_string,que_type=que_type,startup_stage=startup_stage)
    
    db.session.add(que)
    
    db.session.commit()
    
    return jsonify(
        {
            'message': 'Question added successfully',
        }
    )


# route for getting all question just for testing
@auth.route('/getque')
# @jwt_required()
def getque():
    que = Que.query.all()
    json_que = list(map(lambda x: x.to_json(),que))
    count = Que.query.count()
    return jsonify({"que":json_que})




# route for adding answer provided from a user to database
@auth.route('/addans', methods=['POST'])
@jwt_required()
def insert_answer():
    data = request.json
    user_id = get_jwt_identity()
    answers = data.get('answers')

    user = User.query.filter_by(email=user_id).first()
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    if not answers:
        return jsonify({'error': 'No answers provided'}), 400

    for ans_data in answers:
        que_id = ans_data.get('question_id')
        ans_string = ans_data.get('answer')

        que = Que.query.get(que_id)
        
        if not que:
            return jsonify({'error': f'Question {que_id} not found'}), 404

        new_ans = Ans(que_id=que_id, ans_string=ans_string, user_id=user.user_id)
        db.session.add(new_ans)
    
    # Update the is_ans_given field
    user.is_ans_given = True
    db.session.commit()

    return jsonify({'message': 'Answers inserted successfully'}), 201

# route for getting all ans from all user's
@auth.route('/getans')
def getans():
    ans = Ans.query.all()
    json_ans = list(map(lambda x: x.to_json(),ans))
    return jsonify({"ans":json_ans})


# route for deleteing user just for testing
@auth.route('/deluser/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    
    user = User.query.get(user_id)

    
    if not user:
        return jsonify({'error': 'User not found'}), 404

    try:
        
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User and associated entries deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to delete user and associated entries', 'details': str(e)}), 500

#refresh_token route
@auth.route('/refresh-token', methods=['GET'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    return jsonify({'email':current_user},{'access_token': access_token}), 200



# route for getting is_ans_given
@auth.route('/get-is-ans-given',methods=['GET'])
@jwt_required()
def getIsAnsGiven():
    email = get_jwt_identity()
    user = User.query.filter_by(email = email).first()
    return jsonify(
        {
            "isAnsGiven":user.is_ans_given
        }
    )



