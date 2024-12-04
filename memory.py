import sqlite3, time
from datetime import datetime


    
def storeData(quote, joke):
    connect = sqlite3.connect('Client_data.db')
    cur = connect.cursor()
    cur.execute("INSERT INTO jokes (joke) VALUES (:joke)", {'joke': joke})
    cur.execute("INSERT INTO quotes (quote) VALUES (:quote)", {'quote': quote})
    connect.commit()
    connect.close()
    timePassed("quotes")
    timePassed("jokes")

def hasQuote(quote):
    connect = sqlite3.connect('Client_data.db')
    cur = connect.cursor()
    cur.execute("SELECT EXISTS(SELECT 1 FROM quotes WHERE quote = ?)", (quote,))

    result = cur.fetchone()[0]
    connect.close()
    
    if result == 1:
        print("This exists!")
        return True
    else:
        return False
    
def hasJoke(joke):
    connect = sqlite3.connect('Client_data.db')
    cur = connect.cursor()
    cur.execute("SELECT EXISTS(SELECT 1 FROM jokes WHERE joke = ?)", (joke,))

    result = cur.fetchone()[0]
    connect.close()
    
    if result == 1:
        print("This exists!")
        return True
    else:
        return False
    
def delete(id, table):
    connect = sqlite3.connect('Client_data.db')
    cur = connect.cursor()
    cur.execute(f"""DELETE FROM {table} WHERE id =:ID """, {'ID':id})
    connect.commit()
    connect.close()


def update_time_trigger(table):
    connect = sqlite3.connect('Client_data.db')
    cur = connect.cursor()
    cur.execute(f'''
        CREATE TRIGGER IF NOT EXISTS update_all_updated_at
        AFTER INSERT ON jokes 
        BEGIN 
            UPDATE {table}
            SET updated_at = CURRENT_TIMESTAMP;
        END;
    ''')
    connect.commit()
    connect.close()
        

def timePassed(table):
    connect = sqlite3.connect('Client_data.db')
    cur = connect.cursor()
    cur.execute(f"SELECT id, created_at, updated_at FROM {table}")
    rows = cur.fetchall()
    connect.close()
    for row in rows:
        created = datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S")
        updated = datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S")
        id = row[0]
        elapsed_time = (updated-created).days
        if (elapsed_time >= 90):
            delete(id, table)
            
        
    


if __name__  == "__main__":
    timePassed("quotes")
