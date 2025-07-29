
import sqlite3


# ================================= DataBase Function (Notes) ================================= #
def connect():
    '''Internal function'''
    conn = sqlite3.connect("./NotyData.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, noteTitle VARCHAR, noteText VARCHAR );")
    conn.commit()
    conn.close()


def insert(noteTitle, noteText):
    conn = sqlite3.connect("./NotyData.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes VALUES (NULL, ?,?)", (noteTitle, noteText))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("./NotyData.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes")
    rows = cursor.fetchall()
    conn.close()
    return rows


def search(noteTitle=None):
    conn = sqlite3.connect("./NotyData.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes WHERE  noteTitle LIKE ?", (noteTitle,))
    search_res = cursor.fetchall()
    conn.close()
    return search_res


def delete(id):
    conn = sqlite3.connect("./NotyData.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, noteText):
    conn = sqlite3.connect("./NotyData.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE notes SET noteText=? WHERE id=?", (noteText, id))
    conn.commit()
    conn.close()


connect()

# ================================= DataBase Function (Color) ================================= #
def connect_2():
    '''Internal function'''
    conn = sqlite3.connect("./NotyData.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS color (id INTEGER PRIMARY KEY, tbbgcolor VARCHAR, bgcolor VARCHAR);")
    conn.commit()
    cursor.execute("SELECT id FROM color")
    gotColor = cursor.fetchone()
    if not gotColor:
        make("white", "red")
    conn.close()

def make(tbbg, bg):
    '''Internal function'''
    conn = sqlite3.connect("./NotyData.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO color VALUES (NULL, ?, ?)", (tbbg, bg,))
    conn.commit()
    conn.close()

def replace(tbbg=None, bg=None):
    conn = sqlite3.connect("./NotyData.db")
    cursor = conn.cursor()
    if tbbg and not bg:
        cursor.execute("UPDATE color SET tbbgcolor=? WHERE id=?", (tbbg, 1))
        conn.commit()
    elif bg and not tbbg:
        cursor.execute("UPDATE color SET bgcolor=? WHERE id=?", (bg, 1))
        conn.commit()

    conn.close()

def view_2():
    conn = sqlite3.connect("./NotyData.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM color")
    rows = cursor.fetchone()
    conn.close()
    return rows
def delete2(id):
    '''Internal function'''
    conn = sqlite3.connect("./NotyData.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM color WHERE id=?", (id,))
    conn.commit()
    conn.close()
def colorTableDelete():
    '''Internal function'''
    conn = sqlite3.connect("./NotyData.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE color")
    conn.commit()
    conn.close()


connect_2()


