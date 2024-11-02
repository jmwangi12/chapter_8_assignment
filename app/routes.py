from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import RegisterForm, AddProductForm

@app.route('/')
@app.route('/home')
def index():
    """Index URL"""
    return render_template('index.html', title='Index Page')

@app.route('/about_me')
def about_me():
    """About Me URL"""
    return render_template('about_me.html', title='About Me Page')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register URL"""
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'You are requesting to register in {form.username.data}')
        return redirect(url_for('index'))
    return render_template('register.html', title='register', form=form)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    """Add Product URL"""
    form = AddProductForm()
    if form.validate_on_submit():
        flash(f'You are requesting to add the products {form.product_name.data}')
        return redirect(url_for('index'))
    return render_template('add_product.html', title='add product', form=form)

