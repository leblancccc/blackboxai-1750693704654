import sqlite3
import sys
import os

def Connect():
    conn = None
    try:
        db_path = os.path.join(os.path.dirname(__file__), 'taxi_booking_system.db')
        conn = sqlite3.connect(db_path)
    except Exception as e:
        print("Error", e)
    finally:
        return conn
