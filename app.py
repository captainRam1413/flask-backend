
from config import app, db


from auth import auth
from consultantsroute import consultantsroute
from payment import payment
from googleroute import googleroute

app.register_blueprint(auth)
app.register_blueprint(consultantsroute,url_prefix='/consultant')
app.register_blueprint(payment)
app.register_blueprint(googleroute,url_prefix='/google')


@app.route('/')
def home():
    return "<h1>Home</h1>"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

# with app.app_context():
#     db.create_all()
