from flask import Flask, render_template, redirect, url_for
from model import db, Pet
from forms import PetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
app.config['SECRET_KEY'] = 'Pass@123'

db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = PetForm()
    if form.validate_on_submit():
        pet = Pet(name=form.name.data, age=form.age.data, type=form.type.data)
        db.session.add(pet)
        db.session.commit()
        return redirect(url_for('index'))
    pets = Pet.query.all()
    return render_template('view_pets.html', form=form, pets=pets)

if __name__ == '__main__':
    app.run(debug=True)


from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class PetForm(FlaskForm):
    name = StringField('Name')
    age = IntegerField('Age')
    type = StringField('Type')
    submit = SubmitField('Add Pet')

@app.route('/', methods=['GET', 'POST'])
def view_pets():
    form = PetForm()
    if form.validate_on_submit():
        new_pet = {
            "name": form.name.data,
            "age": form.age.data,
            "type": form.type.data
        }
        pets.append(new_pet)
    return render_template('view_pets.html', pets=pets, form=form)
 #code for flask pet app
