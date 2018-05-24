from flask import Flask,render_template, url_for
from forms import RegistrationForm,LoginForm
app = Flask(__name__)
app.config[SECRET_KEY] = '68ee005a8cd58e7d8c4c10cdf5811681'
posts = [
{
"author":"benedict",
"title": "first",
"content":"first dummy content",
"date_posted": "April20, 2018"
},
{
"author":"Jayne",
"title": "second",
"content":"second dummy content",
"date_posted": "April20, 2018"
}
]
@app.route('/')
def home():
    return render_template('home.html',posts = posts)

@app.route('/about')
def about():
    return render_template('about.html',title='kasee')

@app.route("/register")
def register():
    form= RegistrationForm()
    return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':
    app.run(debug=True)
