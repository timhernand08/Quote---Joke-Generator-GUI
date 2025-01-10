import sqlite3
import sys, os 

 
def initialize_db():
    connect = connect_db()
    cur = connect.cursor()
 
    cur.execute('''
        CREATE TABLE IF NOT EXISTS jokes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            joke TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
    ''')
 
    cur.execute('''
        CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quote TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
    ''')

 
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            role TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
    ''')
 
   
    connect.commit()
    connect.close()

def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        application_path = sys._MEIPASS
        print("Pyinstaller bunde")
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
        print("Normal process")
    return os.path.join(application_path, relative_path)
 
def connect_db():
    connect = sqlite3.connect(resource_path('Client_data.db'))
    return connect

#initialize_db()