from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Navya'}
    posts = [
        {
            'author': {'nickname': 'john'},
            'body': 'This is john post'
        },
        {
            'author': {'nickname': 'mery'},
            'body': 'This is mery post'
        }
    ]
    return render_template("index.html", user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login reguested for OpenId = "%s", remember_me=%s '% (form.openid.data, str(form.remember_me.data)))
        return redirect('index')
    return render_template('login.html', form=form, providers=app.config['OPENID_PROVIDERS'])