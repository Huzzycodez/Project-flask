from flask import Flask, render_template 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = "Huzzycodez"
class NameForm(FlaskForm):
    name = StringField("What's your name", validators=[DataRequired()])
    submit = SubmitField("submit")

@app.route('/')

# def index():
 #  return "<h1>Hello world</h1>"
 
def index():
   first_name = "john"
   stuff = "None text is cool"

   favourite_pizza = ["pepperoni", "cheese", "ketchup", 41]
   return render_template("index.html",
     first_name=first_name,
     stuff=stuff,
     favourite_pizza = favourite_pizza)
 
# localhost:5000/user/John
@app.route('/user/<name>')

def user(name):
   return render_template("jinja.html", user_name=name)
  
  #Invalid URL

@app.errorhandler(404)
def page_not_found(e):
   return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
   return render_template("500.html"), 404

@app.route('/name', methods=['GET', 'POST'])
def name():
      name = None
      form = NameForm()
      if form.validate_on_submit():
          name = form.name.Data
          form.name.data = ''

      return render_template("form.html", 
       name = name,
       form = form)
