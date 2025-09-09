import sqlite3

DB_NAME = "bus_tracker.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS buses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bus_number TEXT NOT NULL,
            stop TEXT NOT NULL,
            arrival_time TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_bus(bus_number, stop, arrival_time):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO buses (bus_number, stop, arrival_time) VALUES (?, ?, ?)",
                   (bus_number, stop, arrival_time))
    conn.commit()
    conn.close()

def get_all_buses():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT bus_number, stop, arrival_time FROM buses")
    buses = cursor.fetchall()
    conn.close()
    return buses
