from flask import Blueprint, jsonify , request
from models2 import User,Pswd,Payment,Plan
from config import db
from flask_jwt_extended import create_access_token,get_jwt_identity, jwt_required
import razorpay
from data import secret
import logging

payment = Blueprint('payment', __name__)
logging.basicConfig(level=logging.DEBUG)



@payment.route('/order',methods=['POST'])
@jwt_required()
def order():
    data = request.get_json()
    amount = data.get('amount')
    logging.debug(f"{data}")
    email = get_jwt_identity()
    user = User.query.filter_by(email = email).first()
    note = {
        'name':user.first_name,
        'email': email,
        'phoneNumber':user.phone_number
    }
    order_currency = 'INR'
    client = razorpay.Client(auth=(secret.key_id,secret.key_secret))
    payment = client.order.create({
        'amount':amount,
        'currency': order_currency,
        'payment_capture':1,
        'notes':note
    })
    
    return jsonify(
        {
            'payment':payment
        },200
    )
    
    
@payment.route('/order/validate',methods =['POST'])
@jwt_required()
def verifypayment():
    data = request.get_json()
    order_id = data.get('order_id')
    payment_id = data.get('payment_id')
    signature = data.get('signature')
    amount = data.get('amount')
    client = razorpay.Client(auth=(secret.key_id, secret.key_secret))

    
    out = client.utility.verify_payment_signature({
      'razorpay_order_id': order_id,
      'razorpay_payment_id': payment_id,
      'razorpay_signature': signature
      })
    if not out :
        db.session.rollback()
        return jsonify(
            {
                "message" :"un-successfull"   
            },400
        )
    user = User.query.filter_by(email = get_jwt_identity()).first()
    new_payment = Payment(
        user_id = user.user_id,
        amount = amount,
        status = 'success',
        transaction_id = payment_id,
        order_id = order_id,
        signature = signature,
        plan_id = 1
    )
    
    db.session.add(new_payment)
    db.session.commit()
    return jsonify(
        {
            'message':'successfull',
            'payment' : payment_id
        },200
        )
    