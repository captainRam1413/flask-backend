
from config import app, db


from auth import auth

app.register_blueprint(auth)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)