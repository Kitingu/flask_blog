from flask import Flask,render_template, url_for
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
