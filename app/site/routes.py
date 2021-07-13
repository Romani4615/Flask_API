#import modules/functions/classes that we need for our code to work as intended


from flask import Blueprint, render_template, request, flash, redirect, url_for

from app.models import Animal, db

from app.forms  import newAnimalForm
#defined blueprint

#defining site to a blueprint object(def by flaks) so that this portion of code works as a bunch of websites
#want to use flaks blueprint object 
#CODE I NEED TO MAKE A WORKING WEBSITE
# *site - name (of blueprint)* *template folder is wgere HTML files are located then type folder name* 
site = Blueprint('site', __name__, template_folder='site_templates')
#each webpage is defined/ controlled by a flask route -> which is a python function
#coming from flask-- @ function decorator flask app base URL '/' will take you to homepage 
#blueprint name.route

#when someone connects they can read/accept/recieve or SEND 
@site.route('/', methods=['GET', 'POST']) 
def home():
    form = newAnimalForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            name = form.name.data
            weight = form.weight.data
            height = form.height.data
            climate = form.climate.data
            region = form.region.data
            print('name', 'region')
            #create new animal object in database from form data
            #positional argument//**has to match order of columns
            newanimal = Animal(name, height, weight, climate, region)
            
            #add animal to new database - 2 step
            db.session.add(newanimal)
            db.session.commit()
            
            ##Tell USER WE ADDED SOMETHING
            flash(f'you ahve successfully added the animal {name} to your DATABASE.')
            return redirect(url_for('site.home'))
    
    except:
        raise Exception
        
    return render_template('index.html', form=form) #so template has all info that we setup in forms.py
@site.route('/profile')
def profile():
    return render_template('profile.html')