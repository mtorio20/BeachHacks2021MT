from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from yelp import best_in_town
import pyrebase 

firebaseConfig = {
    'apiKey': "x",
    'authDomain': "x",
    'projectId': "x",
    'storageBucket': "x",
    'messagingSenderId': "x",
    'appId': "x",
    'measurementId': "x",
    "databaseURL" : "x"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()
db=firebase.database()

app = Flask(__name__)
app.config['SECRET_KEY'] = '87ea35d0f73aba5abf87dee9868d3da1'

#calling my best_in_town function using YelpFusion's API to get the top 10 boba shops in San Jose ranked by rating
example = best_in_town('boba', 'Irvine')


@app.route("/")
@app.route("/home", methods=['POST', 'GET'])
def home():
    return render_template('home.html')


def search(food, location):
    food = request.form['food']
    location = request.form['location']
    return render_template('best.html', posts=best_in_town(food,location))

def example(food, location):
    return f'<h1>{food}{location}</h1>'


@app.route("/best")
def best():
    return render_template('best.html', posts=example)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = {'username': form.username.data, 'email': form.email.data}
        auth.create_user_with_email_and_password(form.email.data, form.password.data)
        db.push(user)
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if auth.sign_in_with_email_and_password(form.email.data, form.password.data):
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful', 'danger')
    return render_template('login.html', title='Login', form=form)

