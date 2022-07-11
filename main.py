from flask import Flask, request
import sqlite3

app = Flask(__name__)


@app.route('/phones/create/')
def phone_create():
    phone = request.args['phone']
    name = request.args['name']

    try:
        conn = sqlite3.connect('my_db.db')
        cur = conn.cursor()
        sql = f'''
        INSERT INTO phones
        VALUES ('{phone}', '{name}');
        '''
        cur.execute(sql)
        conn.commit()

    finally:
        conn.close()

    return 'Phones Create'


@app.route('/phones/read/')
def phone_read():

    try:
        conn = sqlite3.connect('my_db.db')
        cur = conn.cursor()
        sql = f'''
        SELECT * FROM phones;
        '''
        cur.execute(sql)
        phones = cur.fetchall()

    finally:
        conn.close()

    return str(phones)


@app.route('/phones/update/')
def phone_update():
    name = request.args['name']
    phone = request.args['phone']

    try:
        conn = sqlite3.connect('my_db.db')
        cur = conn.cursor()
        sql = f'''
        UPDATE phones
        SET ContactName = '{name}'
        WHERE Phone == '{phone}';
        '''
        cur.execute(sql)
        conn.commit()

    finally:
        conn.close()

    return 'Phones Update'


@app.route('/phones/delete/')
def phone_delete():
    phone = request.args['phone']

    try:
        conn = sqlite3.connect('my_db.db')
        cur = conn.cursor()
        sql = f'''
        DELETE FROM phones WHERE Phone == '{phone}';
        '''
        cur.execute(sql)
        conn.commit()

    finally:
        conn.close()

    return 'Phones Delete'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)