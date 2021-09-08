from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, BooleanField,DateField,  SelectField,  TextAreaField, FileField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from dorcas.models import User, Skills, Bio, Edu, Prof, Post,Posts
from flask_login import current_user












class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20, message=('Please we accept a minimum of 5 characters for username'))])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20, message=('Please ensure that your Password combination is more than 8 characters'))])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    terms = BooleanField ('I accept terms & condition',validators=[DataRequired(1)])
    submit = SubmitField ('Sign Up')

    def validate_username(self, username):
        username_exist = User.query.filter_by(username = username.data).first()
        if username_exist:
            raise ValidationError('This Username already Exist, Kindly use a different one.')

    def validate_email(self, email):
        email_exist = User.query.filter_by(email = email.data).first()
        if email_exist:
             raise ValidationError('This Email address already Exist, Kindly use a different one.')



class LoginForm(FlaskForm):

    email = StringField('Email Adreess', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20, message=('Please ensure that your Password combination is more than 8 characters'))])
    remember = BooleanField('Remember me')
    submit = SubmitField ('Login')



class SkillsForm(FlaskForm):

    description = TextAreaField('Description', validators=[DataRequired(), Length(min=10, max=1000, message=('Please we accept more characters for description'))])
    html = StringField('HTML', validators=[DataRequired(), Length(min=1, max=4, message=('Please we accept a minimum of 5 characters for html'))])
    css = StringField('CSS', validators=[DataRequired(), Length(min=1, max=4, message=('Please we accept a minimum of 5 characters for css'))]) 
    python = StringField('Python', validators=[DataRequired(), Length(min=1, max=4, message=('Please we accept a minimum of 5 characters for python'))])
    flask = StringField('Flask', validators=[DataRequired(), Length(min=1, max=4, message=('Please we accept a minimum of 5 characters for flask'))])
    excel = StringField('Excel', validators=[DataRequired(), Length(min=1, max=4, message=('Please we accept a minimum of 5 characters for excel'))])
    mechine_learning = StringField('Mechine_learning', validators=[DataRequired(), Length(min=1, max=4, message=('Please we accept a minimum of 5 characters for mechine_learning'))])
    submit = SubmitField ('skills')




class BioForm(FlaskForm):

    description = TextAreaField('Description', validators=[DataRequired(), Length(min=5, max=500, message=('Please we accept a minimum of 5 characters for description'))])
    country= SelectField(
        'Country of Residency',
        [DataRequired()],
        choices=[
            ('', 'select your country of residency'),
            ('Nigeria', 'Nigeria'),
            ('Ghana', 'Ghana'),
            ('USA', 'USA'),
            ('Canada', 'Canada'),
            ('UK', 'UK'),
           
        ])
   
    city= SelectField(
        'city',
        [DataRequired()],
        choices=[
            ('', 'select your state / city'),
            ('Abia', 'Abia'),
            ('Adamawa', 'Adamawa'),
            ('Akwa Ibom', 'Akwa Ibom'),
            ('Anambra', 'Anambra'),
            ('Bauchi', 'Bauchi'),
            ('Bayelsa', 'Bayelsa'),
            ('Benue', 'Benue'),
            ('Borno', 'Borno'),
            ('Cross River', 'Cross River'),
            ('Delta', 'Delta'),
            ('Ebonyi', 'Ebonyi'),
            ('Edo', 'Edo'),
            ('Ekiti', 'Ekiti'),
            ('Enugu', 'Enugu'),
            ('Gombe', 'Gombe'),
            ('Imo', 'Imo'),
            ('Jigawa', 'Jigawa'),
            ('Kaduna', 'Kaduna'),
            ('Kano', 'Kano'),
            ('Katsina', 'Katsina'),
            ('Kebbi', 'Kebbi'),
            ('Kogi', 'Kogi'),
            ('Kwara', 'Kwara'),
            ('Lagos', 'Lagos'),
            ('Nasarawa', 'Nasarawa'),
            ('Niger', 'Niger'),
            ('Ogun', 'Ogun'),
            ('Ondo', 'Ondo'),
            ('Osun', 'Osun'),
            ('Oyo', 'Oyo'),
            ('Plateau', 'Plateau'),
            ('Rivers', 'Rivers'),
            ('Sokoto', 'Sokoto'),
            ('Taraba', 'Taraba'),
            ('Yobe', 'Yobe'),
            ('Zamfara', 'Zamfara'),
            ('FCT', 'FCT'),
        ])
    w_phone = StringField('Whatsapp Phone', validators=[DataRequired(), Length(min=1, max=20, message=('please enter a correct or valid whatsapp number'))])
    link_url = StringField('Linkedin Url', validators=[DataRequired(), Length(min=1, max=100, message=('Please ensure that you entered a valid Linkedin Url'))])
    submit = SubmitField ('submit')


class EduForm(FlaskForm):


    title = TextAreaField('Degree Title', validators=[DataRequired(), Length(min=5, max=100, message=('Please we accept a minimum of 5 characters for msc title'))])
    year = StringField('Degree Year', validators=[DataRequired(), Length(min=1, max=15, message=('Please we accept a minimum of 5 characters for msc year'))])
    institu = StringField('Degree Institution', validators=[DataRequired(), Length(min=1, max=100, message=('Please we accept a minimum of 5 characters for msc institution'))]) 
    country = SelectField(
            'Country',
            [DataRequired()],
            choices=[
                ('', 'select country'),
                ('Nigeria', 'Nigeria'),
                ('Ghana', 'Ghana'),
                ('USA', 'USA'),
                ('Canada', 'Canada'),
                ('UK', 'UK')
            
            ])

    city= SelectField(
            'city',
            [DataRequired()],
            choices=[
                ('', 'select state / city'),
                ('London', 'London'),
                ('Bradford', 'Bradford'),
                ('Akwa Ibom', 'Akwa Ibom'),
                ('Anambra', 'Anambra'),
                ('Bauchi', 'Bauchi'),
                ('Bayelsa', 'Bayelsa'),
                ('Benue', 'Benue'),
                ('Borno', 'Borno'),
                ('Cross River', 'Cross River'),
                ('Delta', 'Delta'),
                ('Ebonyi', 'Ebonyi'),
                ('Edo', 'Edo'),
                ('Ekiti', 'Ekiti'),
                ('Enugu', 'Enugu'),
                ('Gombe', 'Gombe'),
                ('Imo', 'Imo'),
                ('Jigawa', 'Jigawa'),
                ('Kaduna', 'Kaduna'),
                ('Kano', 'Kano'),
                ('Katsina', 'Katsina'),
                ('Kebbi', 'Kebbi'),
                ('Kogi', 'Kogi'),
                ('Kwara', 'Kwara'),
                ('Lagos', 'Lagos'),
                ('Nasarawa', 'Nasarawa'),
                ('Niger', 'Niger'),
                ('Ogun', 'Ogun'),
                ('Ondo', 'Ondo'),
                ('Osun', 'Osun'),
                ('Oyo', 'Oyo'),
                ('Plateau', 'Plateau'),
                ('Rivers', 'Rivers'),
                ('Sokoto', 'Sokoto'),
                ('Taraba', 'Taraba'),
                ('Yobe', 'Yobe'),
                ('Zamfara', 'Zamfara'),
                ('FCT', 'FCT'),
            ])

    submit = SubmitField ('submit')




class ProfForm(FlaskForm):


    title = TextAreaField('Work Title', validators=[DataRequired(), Length(min=5, max=100, message=('Please we accept a minimum of 5 characters for  title'))])
    year = StringField('Work Year', validators=[DataRequired(), Length(min=5, max=25, message=('Please we accept a minimum of 5 characters for year'))])
    duty1 = TextAreaField('Job Duty1', validators=[DataRequired(), Length(min=5, max=500, message=('Please we accept a minimum of 5 characters for  duty'))])
    duty2 = TextAreaField('Job Duty2', validators=[DataRequired(), Length(min=5, max=500, message=('Please we accept a minimum of 5 characters for  duty'))])
    duty3 = TextAreaField('Job Duty3', validators=[DataRequired(), Length(min=5, max=500, message=('Please we accept a minimum of 5 characters for  '))])
    company = TextAreaField('Work Company', validators=[DataRequired(), Length(min=1, max=100, message=('Please we accept a minimum of 5 characters for company'))]) 
    country = SelectField(
            'Country',
            [DataRequired()],
            choices=[
                ('', 'select country'),
                ('Nigeria', 'Nigeria'),
                ('Ghana', 'Ghana'),
                ('USA', 'USA'),
                ('Canada', 'Canada'),
                ('UK', 'UK')
            
            ])

    city= SelectField(
            'city',
            [DataRequired()],
            choices=[
                ('', 'select state / city'),
                ('London', 'London'),
                ('Bradford', 'Bradford'),
                ('Akwa Ibom', 'Akwa Ibom'),
                ('Anambra', 'Anambra'),
                ('Bauchi', 'Bauchi'),
                ('Bayelsa', 'Bayelsa'),
                ('Benue', 'Benue'),
                ('Borno', 'Borno'),
                ('Cross River', 'Cross River'),
                ('Delta', 'Delta'),
                ('Ebonyi', 'Ebonyi'),
                ('Edo', 'Edo'),
                ('Ekiti', 'Ekiti'),
                ('Enugu', 'Enugu'),
                ('Gombe', 'Gombe'),
                ('Imo', 'Imo'),
                ('Jigawa', 'Jigawa'),
                ('Kaduna', 'Kaduna'),
                ('Kano', 'Kano'),
                ('Katsina', 'Katsina'),
                ('Kebbi', 'Kebbi'),
                ('Kogi', 'Kogi'),
                ('Kwara', 'Kwara'),
                ('Lagos', 'Lagos'),
                ('Nasarawa', 'Nasarawa'),
                ('Niger', 'Niger'),
                ('Ogun', 'Ogun'),
                ('Ondo', 'Ondo'),
                ('Osun', 'Osun'),
                ('Oyo', 'Oyo'),
                ('Plateau', 'Plateau'),
                ('Rivers', 'Rivers'),
                ('Sokoto', 'Sokoto'),
                ('Taraba', 'Taraba'),
                ('Yobe', 'Yobe'),
                ('Zamfara', 'Zamfara'),
                ('FCT', 'FCT'),
            ])
   

    submit = SubmitField ('submit')


class PostedForm(FlaskForm):

    title = StringField('Work Title', validators=[DataRequired(), Length(min=5, max=100, message=('Please we accept a minimum of 5 characters for  title'))])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=5, max=250, message=('Please we accept a minimum of 5 characters for description'))])
    file = FileField('Upload Application/ Project', validators=[FileAllowed(['rar','zip', 'mp3','mp4', 'xlsx', 'xlsb'])])
    screenshot = FileField('Upload Screenshot/ Project', validators=[FileAllowed(['jpg','jpeg', 'png','jfif','pdf'])])
    submit = SubmitField ('Upload')


class EditInfoForm(FlaskForm):

    title = StringField('Work Title', validators=[DataRequired(), Length(min=5, max=100, message=('Please we accept a minimum of 5 characters for  title'))])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=5, max=250, message=('Please we accept a minimum of 5 characters for description'))])
    submit = SubmitField ('Upload')


class FileUpdateForm(FlaskForm):

    file = FileField('Upload Application/ Project', validators=[FileAllowed(['rar','zip', 'mp3','mp4'])])
    submit = SubmitField ('Upload')

class ScreenUpdateForm(FlaskForm):

    screenshot = FileField('Upload Screenshot/ Project', validators=[FileAllowed(['jpg','jpeg', 'png','jfif','pdf'])])
    submit = SubmitField ('Upload')


