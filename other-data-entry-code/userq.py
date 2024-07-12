import json
from config import db,app
from models2 import Userque  # make sure to import your model

def insert_questions(json_data):
    try:
        questions = json.loads(json_data)
        for question in questions:
            que_type = question['que_type']
            que_string = question['que_string']
            new_question = Userque(que_type=que_type, que_string=que_string)
            db.session.add(new_question)
        db.session.commit()
        print("Questions inserted successfully")
    except Exception as e:
        db.session.rollback()
        print(f"An error occurred: {e}")

# Example JSON data
json_data = '''
[{"que_type":"Personal Background and Experience","que_string":"What is your highest level of education?"},
 {"que_type":"Personal Background and Experience","que_string":"Do you have any previous entrepreneurial experience? Please describe."},
 {"que_type":"Skills and Competencies","que_string":"What technical skills do you possess relevant to your startup idea?"},
 {"que_type":"Skills and Competencies","que_string":"Have you had experience in managing business operations or finances?"},
 {"que_type":"Industry Knowledge","que_string":"How familiar are you with the industry you plan to enter?"},
 {"que_type":"Industry Knowledge","que_string":"What research have you conducted on the market trends and customer needs?"},
 {"que_type":"Business Idea","que_string":"Briefly describe your business idea."},
 {"que_type":"Business Idea","que_string":"What makes your idea unique compared to existing solutions?"},
 {"que_type":"Financial Readiness","que_string":"Do you have personal savings or financial backing to support your startup?"},
 {"que_type":"Financial Readiness","que_string":"What are your plans for funding your business?"},
 {"que_type":"Network and Resources","que_string":"Do you have mentors or advisors in your desired industry?"},
 {"que_type":"Network and Resources","que_string":"How strong is your professional network in this field?"},
 {"que_type":"Motivation and Commitment","que_string":"Why do you want to start this business?"},
 {"que_type":"Motivation and Commitment","que_string":"How much time can you dedicate to your startup each week?"},
 {"que_type":"Market Research","que_string":"Have you validated your idea with potential customers?"},
 {"que_type":"Market Research","que_string":"What have you learned about your competitors?"},
 {"que_type":"Legal and Regulatory Awareness","que_string":"Are you familiar with the legal requirements for starting a business in your region?"},
 {"que_type":"Legal and Regulatory Awareness","que_string":"Do you have plans to protect your intellectual property?"},
 {"que_type":"Business Plan Development","que_string":"Have you developed a business model for your startup?"},
 {"que_type":"Business Plan Development","que_string":"What is your go-to-market strategy?"}]
'''

# Call the function with the JSON data


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        insert_questions(json_data)
        print("Database populated successfully!")
