from datetime import datetime
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from dorcas import db, login_manager, app
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
  return User.query.filter_by(id=user_id).first()   


class User(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    terms = db.Column(db.String(255), nullable=False)
    skill_status = db.Column(db.String(255), nullable=True, default =0)
    bio_status = db.Column(db.String(255), nullable=True, default =0)
    edu_status = db.Column(db.String(255), nullable=True, default =0)
    pro_status = db.Column(db.String(255), nullable=True, default =0)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())



class Skills(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    html = db.Column(db.String(255), nullable=False)
    css= db.Column(db.String(255), nullable=False)
    python = db.Column(db.String(255), nullable=False)
    flask = db.Column(db.String(255), nullable=False)
    excel = db.Column(db.String(255), nullable=False)
    mechine_learning = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
  
class Bio(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(255), nullable=False)
    city= db.Column(db.String(255), nullable=False)
    w_phone = db.Column(db.String(255), nullable=False)
    link_url = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())

class Edu(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    msc_title = db.Column(db.String(255), nullable=False)
    msc_year = db.Column(db.String(255), nullable=False)
    msc_institu = db.Column(db.String(255), nullable=False)
    msc_country= db.Column(db.String(255), nullable=False)
    msc_city = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())


class Education(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    year = db.Column(db.String(255), nullable=False)
    institu = db.Column(db.String(255), nullable=False)
    country= db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())

class Prof(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    year = db.Column(db.String(255), nullable=False)
    company = db.Column(db.String(255), nullable=False)
    country= db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())


class Professional(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    duty1 = db.Column(db.String(255), nullable=True)
    duty2 = db.Column(db.String(255), nullable=True)
    duty3 = db.Column(db.String(255), nullable=True)
    year = db.Column(db.String(255), nullable=False)
    company = db.Column(db.String(255), nullable=False)
    country= db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())


class Post(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), nullable=False)
    title = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), unique=True, nullable=False)
    file = db.Column(db.String(255), unique=True, nullable=False)
    screenshot = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
   

class Posts(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    file = db.Column(db.String(255), unique=True, nullable=False)
    screenshot = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())


class Upload(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    file = db.Column(db.String(255), nullable=False)
    screenshot = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())