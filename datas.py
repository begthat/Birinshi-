import sqlite3


db = sqlite3.connect('tgbot.db')
cursor = db.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS users(
#                id INTEGER,
#                name TEXT,
#                phone_number TEXT,
#                address TEXT)
# ''')
# db.commit()


async def save_user(id,name,phone,adress):
    cursor.execute('''
INSERT INTO users(id,name,phone_number,address)
                         VALUES(?,?,?,?)
''',(id,name,phone,adress,))
    db.commit()

async def show_user():
    cursor.execute('SELECT * FROM users')
    datass=cursor.fetchall()
    return datass