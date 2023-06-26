from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'ab82c0866ce0193c68474c733c75d998'

posts = [
    {
        'author': 'Krisztian Markella',
        'title': 'Blog Post 1',
        'content': 'First Blog Post',
        'date_posted': 'June 25, 2023',
    },
    {
        'author': 'Christian Markella',
        'title': 'Blog Post 2',
        'content': 'Second Blog Post',
        'date_posted': 'June 26, 2023',
    },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(message=f"Account created for {form.username.data}!", category='success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'mamaMango':
            flash(message=f"You have been logged in !", category='success')
            return redirect(url_for('home'))
        else:
            flash(message='Login unsuccessful, please check email and password', category='danger')

    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)
