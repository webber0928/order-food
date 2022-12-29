import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_item(item_id):
    conn = get_db_connection()
    item = conn.execute('SELECT * FROM menu WHERE id = ?',
                        (item_id,)).fetchone()
    conn.close()
    if item is None:
        abort(404)
    return item


@app.route('/')
def index():
    # return render_template('aaa.html')
    conn = get_db_connection()
    menu = conn.execute('SELECT * FROM menu').fetchall()
    conn.close()
    return render_template('index.html', menu=menu)


@app.route('/item/<int:item_id>')
def item(item_id):
    item = get_item(item_id)
    return render_template('item.html', item=item)


@app.route('/create', methods=('GET', 'POST'))
def create_item():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        img = request.form['img']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute(
                'INSERT INTO menu (title, price, img) VALUES (?, ?, ?)', (title, int(price), img))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    item = get_item(id)

    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        img = request.form['img']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute(
                'UPDATE menu SET title = ?, price = ?, img = ? WHERE id = ?', (title, price, img, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', item=item)


# @app.route('menu/<int:id>/delete', methods=('POST',))
# def delete(id):
#     item = get_item(id)
#     conn = get_db_connection()
#     conn.execute('DELETE FROM menu WHERE id = ?', (id,))
#     conn.commit()
#     conn.close()
#     flash('"{}" was successfully deleted!'.format(item['title']))
#     return redirect(url_for('index'))
