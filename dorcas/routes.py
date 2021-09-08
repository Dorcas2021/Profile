import os
import random
import secrets
from flask import render_template, request, session, logging, url_for, redirect, flash, send_from_directory, current_app
from flask.templating import render_template_string
from dorcas import app, db, bcrypt
from dorcas.forms import RegistrationForm, LoginForm, SkillsForm, BioForm, EduForm, ProfForm,PostedForm, EditInfoForm, FileUpdateForm,  ScreenUpdateForm
from flask_login import login_user, current_user, logout_user, login_required
from dorcas.models import User, Skills, Bio, Education, Professional, Post, Posts, Upload





  # this is a function to upload the user ID Card
def save_app_file(file):
  random_hex = secrets.token_hex(8)
  _, f_ext = os.path.splitext(file.filename)
  picture_fn = random_hex + f_ext
  picture_path = os.path.join(app.root_path, 'static/user_uploads', picture_fn)
  file.save(picture_path)
  return picture_fn
  
# this is a function to upload the user Prfile Picture 
def save_screenshot(screenshot):
  random_hex = secrets.token_hex(8)
  _, f_ext = os.path.splitext(screenshot.filename)
  picture_fn = random_hex + f_ext
  picture_path = os.path.join(app.root_path, 'static/user_uploads', picture_fn)
  screenshot.save(picture_path)
  return picture_fn




@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
      user = User.query.filter_by(email=form.email.data).first()
      if user and bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user)
        next_page = request.args.get('next')
        return redirect (next_page) if next_page else redirect (url_for('profile'))
      else:
           flash(f'Incorrect or wrong Email / Password Combination! ', 'danger')
    return render_template('/login.html',title='Login', form=form)
        

@app.route('/registration', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password,terms=form.terms.data )
        db.session.add(user)
        db.session.commit()
        flash(f'Account Created for {form.username.data} Successfully !', 'success')
        return redirect ('login')
    return render_template('registration.html', title = 'Register', form=form)
    


@app.route('/profile')
@login_required
def profile():
  skills=Skills.query.filter_by(email=current_user.email)
  bios=Bio.query.filter_by(email=current_user.email)
  edus=Education.query.filter_by(email=current_user.email).order_by(Education.created_at.desc())
  profs=Professional.query.filter_by(email=current_user.email).order_by(Professional.created_at.desc())
  page = request.args.get('page', 1, type=int)
  posts = Upload.query.order_by(Upload.created_at.desc()).paginate(page = page,  per_page=3)
  return render_template('/profile.html', title='profile', skills=skills, bios=bios, edus=edus, profs=profs, posts=posts)


@app.route('/skills', methods=['GET', 'POST'])
def skills():
    skill_content= Skills.query.filter_by(email=current_user.email).first()
    form = SkillsForm()
    if form.validate_on_submit():
        skills = Skills(email=current_user.email, description=form.description.data, html=form.html.data, css=form.css.data, flask=form.flask.data, python=form.python.data, excel=form.excel.data, mechine_learning=form.mechine_learning.data)
        current_user.skill_status = 1
        db.session.add(skills)
        db.session.commit()
        flash(f'skills Created for Successfully !', 'success')
        return redirect ('profile')
    return render_template('skills.html', title = 'Skills', form=form)


@app.route('/editskills', methods=['GET', 'POST'])
def editskills():
    skill_content= Skills.query.filter_by(email=current_user.email).first()
    form = SkillsForm()
    if form.validate_on_submit():

      skill_content.description = form.description.data
      skill_content.html = form.html.data
      skill_content.css = form.css.data
      skill_content.flask = form.flask.data
      skill_content.python = form.python.data
      skill_content.excel = form.excel.data
      skill_content.mechine_learning = form.mechine_learning.data
      
      db.session.commit()
      flash(f'skills Created for Successfully !', 'success')
      return redirect ('profile')
    elif request.method=='GET':
      form.description.data = skill_content.description
      form.html.data = skill_content.html
      form.css.data = skill_content.css
      form.flask.data = skill_content.flask
      form.python.data = skill_content.python
      form.excel.data = skill_content.excel
      form.mechine_learning.data = skill_content.mechine_learning

    return render_template('skills.html', title = 'Skills', form=form)



@app.route('/bio', methods=['GET', 'POST'])
def bio():
    
    form = BioForm()
    if form.validate_on_submit():
        bio=Bio(email=current_user.email, description=form.description.data, country=form.country.data, city=form.city.data, w_phone=form.w_phone.data, link_url=form.link_url.data)
        current_user.bio_status = 1
        db.session.add(bio)
        db.session.commit()
        flash(f'bio Created for Successfully !', 'success')
        return redirect ('profile')
    return render_template('bio.html', title = 'Bio', form=form)



@app.route('/editbio', methods=['GET', 'POST'])
def editbio():
    bio_content= Bio.query.filter_by(email=current_user.email).first()
    form = BioForm()
    if form.validate_on_submit():

      bio_content.description = form.description.data
      bio_content.country = form.country.data
      bio_content.city = form.city.data
      bio_content.w_phone = form.w_phone.data
      bio_content.link_url = form.link_url.data
      
      
      db.session.commit()
      flash(f'bio Created for Successfully !', 'success')
      return redirect ('profile')
    elif request.method=='GET':
      form.description.data = bio_content.description
      form.country.data = bio_content.country
      form.city.data = bio_content.city
      form.w_phone.data = bio_content.w_phone
      form.link_url.data = bio_content.link_url
      
    return render_template('editbio.html', title = 'Bio', form=form)



@app.route('/edu', methods=['GET', 'POST'])
def edu():
  
  edus=Education.query.filter_by(email=current_user.email).order_by(Education.created_at.desc())

  form = EduForm()
  if form.validate_on_submit():
      edu = Education(email=current_user.email, title=form.title.data, year=form.year.data, institu=form.institu.data, country=form.country.data, city=form.city.data)
      current_user.edu_status = 1
      db.session.add(edu)
      db.session.commit()
      flash(f'edu Created for Successfully !', 'success')
      return redirect ('profile')
  return render_template('edu.html', title = 'Edu', form=form, edus=edus)


@app.route('/editedu/<int:edu_id>/update', methods=['GET', 'POST'])
def editedu(edu_id):
  edus= Education.query.filter_by(email=current_user.email).first()
  form = EduForm()
  edu=Education.query.get(edu_id)
  if form.validate_on_submit():

    edu.title = form.title.data
    edu.country = form.country.data
    edu.city = form.city.data
    edu.institu = form.institu.data
    edu.year = form.year.data
    db.session.commit()
    flash(f'edu Updated Successfully !', 'success')
    return redirect (url_for('edu', edu_id = edu.id))
  elif request.method=='GET':
    form.title.data = edu.title
    form.country.data = edu.country
    form.city.data = edu.city
    form.institu.data = edu.institu
    form.year.data = edu.year
    
  return render_template('editedu.html', title = 'Bio', form=form, edus=edus)


@app.route('/delete_edu/<int:edu_id>/delete', methods=['GET', 'POST'])
def delete_edu(edu_id):

  form = EduForm()
  edu=Education.query.get(edu_id)
  db.session.delete(edu)
  db.session.commit()
  flash(f'edu deleted Successfully !', 'success')
  return redirect (url_for('edu'))



@app.route('/prof', methods=['GET', 'POST'])
def prof():
  
  profs=Professional.query.filter_by(email=current_user.email).order_by(Professional.created_at.desc())

  form = ProfForm()
  if form.validate_on_submit():
      prof = Professional(email=current_user.email, title=form.title.data, year=form.year.data, company=form.company.data, duty1=form.duty1.data, duty2=form.duty2.data, duty3=form.duty3.data, country=form.country.data, city=form.city.data)
      current_user.prof_status = 1
      db.session.add(prof)
      db.session.commit()
      flash(f'prof Created for Successfully !', 'success')
      return redirect ('profile')
  return render_template('prof.html', title = 'Prof', form=form, profs=profs)


@app.route('/editprof/<int:prof_id>/update', methods=['GET', 'POST'])
def editprof(prof_id):
  profs= Professional.query.filter_by(email=current_user.email).first()
  form = ProfForm()
  prof=Professional.query.get(prof_id)
  if form.validate_on_submit():

    prof.title = form.title.data
    prof.country = form.country.data
    prof.city = form.city.data
    prof.duty1 = form.duty1.data
    prof.duty2 = form.duty2.data
    prof.duty3 = form.duty3.data
    prof.company = form.company.data
    prof.year = form.year.data
    db.session.commit()
    flash(f'prof Updated Successfully !', 'success')
    return redirect (url_for('prof', prof_id = prof.id))
  elif request.method=='GET':
    form.title.data = prof.title
    form.country.data = prof.country
    form.city.data = prof.city
    form.duty1.data = prof.duty1
    form.duty2.data = prof.duty2
    form.duty3.data = prof.duty3
    form.company.data = prof.company
    form.year.data = prof.year
    
  return render_template('editprof.html', title = 'Bio', form=form, profs=profs)


@app.route('/delete_prof/<int:prof_id>/delete', methods=['GET', 'POST'])
def delete_prof(prof_id):

  form = ProfForm()
  prof=Professional.query.get(prof_id)
  db.session.delete(prof)
  db.session.commit()
  flash(f'prof deleted Successfully !', 'success')
  return redirect (url_for('prof'))


@app.route('/post', methods=['GET', 'POST'])
def posted():
    form = PostedForm()
    if form.validate_on_submit():
        file = save_app_file(form.file.data)
        screenshot = save_screenshot(form.screenshot.data)
        po = Upload(email=current_user.email, title=form.title.data, description=form.description.data, file= file, screenshot=screenshot)
        db.session.add(po)
        db.session.commit()
        flash(f'Your application/project has been uploaded!','success')
        return redirect (url_for('profile')) 
    return render_template('post.html', title = 'Register', form=form)



@app.route('/')
def index():
  skills=Skills.query.filter_by(email='dorcas@gmail.com')
  bios=Bio.query.filter_by(email='dorcas@gmail.com')
  edus=Education.query.filter_by(email='dorcas@gmail.com').order_by(Education.created_at.desc())
  profs=Professional.query.filter_by(email='dorcas@gmail.com').order_by(Professional.created_at.desc())
  page = request.args.get('page', 1, type=int)
  posts = Upload.query.order_by(Upload.created_at.desc()).paginate(page = page,  per_page=3)
  return render_template('/index.html',title = " welcome", skills = skills, bios=bios, edus=edus, profs=profs, posts=posts)

@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    # Appending app path to upload folder path within app root folder
    uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'] )
    picture_path = os.path.join(app.root_path, 'static/user_uploads',)
    # Returning file from appended path
    return send_from_directory(picture_path, filename, as_attachment=True)


@app.route('/editinfo/<int:post_id>/update', methods=['GET', 'POST'])
def editinfo(post_id):
  post= Upload.query.filter_by(email=current_user.email).first()
  form = EditInfoForm()
  post=Upload.query.get(post_id)
  if form.validate_on_submit():

    post.title = form.title.data
    post.description = form.description.data
    db.session.commit()
    flash(f'post Updated Successfully !', 'success')
    return redirect (url_for('profile', post_id = post.id))
  elif request.method=='GET':
    form.title.data = post.title
    form.description.data = post.description
    
  return render_template('edit_info.html', title = 'EditInfo', form=form, post=post)



@app.route('/updatefile/<int:post_id>/update',methods=['GET', 'POST'])
@login_required
def updatefile(post_id):
   form = FileUpdateForm()
   if form.validate_on_submit():

    if form.file.data:
      picture_fil = save_app_file(form.file.data)  
      update_post = Upload.query.get(post_id)
      update_post.file = picture_fil
      db.session.commit()
    return redirect (url_for('profile'))
   else:
    return render_template('/updatefile.html', title='Update File', form = form)



@app.route('/updatescreen/<int:post_id>/update',methods=['GET', 'POST'])
@login_required
def updatescreenshot(post_id):
   form = ScreenUpdateForm()
   if form.validate_on_submit():

    if form.screenshot.data:
      picture_fil = save_screenshot(form.screenshot.data)  
      update_post = Upload.query.get(post_id)
      update_post.screenshot = picture_fil
      db.session.commit()
    return redirect (url_for('profile'))
   else:
    return render_template('/updatescreen.html', title='Update Screen', form = form)


@app.route('/delete_post/<int:post_id>/delete', methods=['GET', 'POST'])
def delete_post(post_id):

  # form = EduForm()
  post=Upload.query.get(post_id)
  db.session.delete(post)
  db.session.commit()
  flash(f'post deleted Successfully !', 'success')
  return redirect (url_for('profile'))





@app.route('/logout', methods=['GET', 'POST'])
def logout():
  logout_user()
  return redirect(url_for('index'))

 