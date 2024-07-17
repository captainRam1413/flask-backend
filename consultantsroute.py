from flask import Blueprint,jsonify,request
import logging
from models2 import ConToUser, Consultant,ConPswd, User
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, create_refresh_token # type: ignore
from config import db


consultantsroute = Blueprint('consultantsroute', __name__)
logging.basicConfig(level=logging.DEBUG)

@consultantsroute.route('/login-consultant',methods=['POST'])
def loginconsultant():  
    data = request.get_json()
    email = data.get('email')
    paswd =data.get('password')
    
    consultant = Consultant.query.filter_by(email = email).first()
    
    if consultant and consultant.con_pswd.pswd== paswd:
        access_token = create_access_token(identity=consultant.email)
        refresh_token = create_refresh_token(identity=consultant.email)
        return jsonify(
            {
                'access_token':access_token,
                'email':consultant.email,
                'refresh_token':refresh_token
            },200
        )
    return jsonify(
        {
            'msg':'user not found'
        },404
    )
    
@consultantsroute.route('/create-consultant', methods=['POST'])
def createconsultant():
    try:
        data = request.get_json()
        logging.debug(f"Received data: {data}")
        email = data.get('email')
        password = data.get('password')
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        phone = data.get('phone')
        consulting_field = data.get('consulting_field')
        experience_years = data.get('experience_years')

        consultant = Consultant.query.filter_by(email=email).first()
        if consultant:
            return jsonify({'message': 'User already exists'}), 403

        con_pswd = ConPswd(pswd = password)
        new_consultant = Consultant(
            first_name=first_name,
            last_name=last_name,
            email=email,
            experience_years=experience_years,
            consulting_field=consulting_field,
            phone=phone
            # con_pswd = con_pswd
        )
        new_consultant.con_pswd = con_pswd

        db.session.add(new_consultant)
        db.session.commit()

        return jsonify({'message': 'User created successfully'}), 200

    except Exception as e:
        db.session.rollback()
        logging.error(f"Error occurred: {e}")
        return jsonify({'message': str(e)}), 500

    
@consultantsroute.route('/get-consultant')
@jwt_required()
def getconsultant():
    consultants = Consultant.query.all()
    json_consultant = list(map(lambda x:x.to_json(),consultants))
    return jsonify(
        {
            'consultants':json_consultant
        }
    )

@consultantsroute.route('/get-consultant-profile')
@jwt_required()
def getconsultantprofile():
    email = get_jwt_identity()
    consultant = Consultant.query.filter_by(email = email).first()
    return jsonify(
        {
            'consultant':consultant.to_json()
            }
        )

@consultantsroute.route('/get-user-consultant-list')
@jwt_required()
def getuserconsultantlist():
    email = get_jwt_identity()
    consultant = Consultant.query.filter_by(email = email).first()
    id = consultant.consultant_id
    logging.debug(f"Received data: {id}")
    jsondata = []
    contouser = ConToUser.query.filter_by(consultant_id = id).all()
    
    for users in contouser:
        userid = users.user_id
        logging.debug(f"Received data: {userid}")
        logging.debug(f"Received data: {users}")
        user = User.query.filter_by(user_id = userid).first()
        userdata = {"user_id":user.user_id,
                    "firstName":user.first_name,
                    "lastName":user.last_name,
                    "email":user.email}
        jsondata.append(userdata)
    
    # json_contouser = list(map(lambda x:x.to_json(),contouser))
    return jsonify(
        {
            # 'user_list':json_contouser
            'user_list':jsondata
        }
        )
    
@consultantsroute.route('/get-userprofile-consultant',methods=['POST'])
@jwt_required()
def getuserprofileconsultant():
    data = request.get_json()
    user_id = data.get('user_id')
    user = User.query.filter_by(user_id = user_id).first()
    return jsonify(
        {
            'user':user.to_json()
        }
    )
    

    

