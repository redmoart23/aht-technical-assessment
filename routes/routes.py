from flask import Blueprint, render_template

inventory = Blueprint('inventory', __name__)


@inventory.route('/')
def index():
    return render_template('index.html')


@inventory.route('/add')
def add():
    return render_template('add.html')


@inventory.route('/edit/<int:id>')
def edit(id):
    return render_template('edit.html')


@inventory.route('/delete/<int:id>')
def delete(id):
    return render_template('delete.html')