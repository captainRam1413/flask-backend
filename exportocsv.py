import csv
from config import db,app
from models2 import Ans, User, Userans

def export_user_answers_to_csv(user_id):
    # Query all answers by the specified user_id
    answers = Ans.query.filter_by(user_id=user_id).all()
    edu_ans = Userans.query.filter_by(user_id=user_id).all()
    
    # Define the CSV file name
    output_file = 'user_answers.csv'
    output_file2 ='user_edu_ans.csv'
    
    # Write the data to CSV
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['answer_id', 'question_id', 'question', 'answer', 'user_id', 'first_name', 'last_name', 'email'])
        # Write the data
        for answer in answers:
            question = answer.que
            user = User.query.get(answer.user_id)  # Fetch user by user_id
            if question and user:  # Ensure related objects are not None
                writer.writerow([
                    answer.ans_id,
                    question.que_id,
                    question.que_string,
                    answer.ans_string,
                    user.user_id,
                    user.first_name,
                    user.last_name,
                    user.email
                ])
                
    with open(output_file2, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['answer_id', 'question_id', 'question', 'answer', 'user_id', 'first_name', 'last_name', 'email'])
        # Write the data
        for answer in edu_ans:
            question = answer.userque
            user = answer.user
            # user = User.query.get(answer.user_id)  # Fetch user by user_id
            if question and user:  # Ensure related objects are not None
                writer.writerow([
                    answer.ans_id,
                    question.que_id,
                    question.que_string,
                    answer.ans_string,
                    user.user_id,
                    user.first_name,
                    user.last_name,
                    user.email
                ])
    
    print(f'Data exported to {output_file}')

if __name__ == "__main__":
    user_id = 1  # Replace with the desired user ID
    with app.app_context():  # Ensure this runs in an app context if required
        export_user_answers_to_csv(user_id)
