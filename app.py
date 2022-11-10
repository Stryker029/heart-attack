from flask import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import func
from flask_login import UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


with app.app_context():
	db.create_all()

class Quote(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	quote = db.Column(db.String(255), nullable=False)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self):
		return '<Quote %r>' % self.id
		
class User(db.Model, UserMixin):
    userid = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))

@app.route('/', methods=['POST', 'GET'])
def index():
	return render_template('index.html')    
	
@app.route('/create', methods=['POST', 'GET'])
def create():
	return render_template('create.html')
	
@app.route('/profile', methods=['POST', 'GET'])
def profile():
	return render_template('profile.html')

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=42069, debug=True)
	
