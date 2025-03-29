from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.inventory import Inventory
from utils.db import db

inventory = Blueprint('inventory', __name__)


@inventory.route('/')
def index():

    items = Inventory.query.all()

    return render_template('index.html', items=items)


@inventory.route('/add', methods=['GET', 'POST'])
def add():

    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        mac_address = request.form['mac_address']
        serial_number = request.form['serial_number']
        manufacturer = request.form['manufacturer']
        description = request.form['description']

        new_item = Inventory(name, price, mac_address,
                             serial_number, manufacturer, description)
        db.session.add(new_item)
        db.session.commit()

        flash('Item added successfully', 'success')

        return redirect(url_for('inventory.index'))

    return render_template('add.html')


@inventory.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    item = Inventory.query.get(id)

    if request.method == 'POST':

        item.name = request.form['name']
        item.price = request.form['price']
        item.mac_address = request.form['mac_address']
        item.serial_number = request.form['serial_number']
        item.manufacturer = request.form['manufacturer']
        item.description = request.form['description']

        db.session.commit()

        flash('Item updated successfully', 'success')

        return redirect(url_for('inventory.index'))

    return render_template('edit.html', item=item)


@inventory.route('/delete/<int:id>')
def delete(id):

    item = Inventory.query.get(id)
    db.session.delete(item)
    db.session.commit()

    flash('Item deleted successfully', 'success')

    return redirect(url_for('inventory.index'))
