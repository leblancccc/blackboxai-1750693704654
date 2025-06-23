import sqlite3
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dbms.connection import Connect

def create_tables():
    conn = None
    try:
        conn = Connect()
        cursor = conn.cursor()

        # Create drivers table with vehicle type
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS drivers (
            did INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            mobile TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            license TEXT NOT NULL,
            password TEXT NOT NULL,
            driverstatus TEXT NOT NULL,
            vehicletype TEXT NOT NULL
        )
        """)

        # Create customers table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            cid INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            dob TEXT NOT NULL,
            gender TEXT NOT NULL,
            mobile TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            address TEXT NOT NULL,
            password TEXT NOT NULL,
            credit TEXT NOT NULL,
            status TEXT NOT NULL
        )
        """)

        # Create booking table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS booking (
            bookingid INTEGER PRIMARY KEY,
            pickupaddress TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            dropoffaddress TEXT NOT NULL,
            bookingstatus TEXT NOT NULL,
            cid INTEGER,
            did INTEGER,
            FOREIGN KEY (cid) REFERENCES customers (cid),
            FOREIGN KEY (did) REFERENCES drivers (did)
        )
        """)

        # Create billing table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS billing (
            billid INTEGER PRIMARY KEY,
            bookingid INTEGER NOT NULL,
            total REAL NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY (bookingid) REFERENCES booking (bookingid)
        )
        """)

        # Create admin table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS admin (
            adminid INTEGER PRIMARY KEY,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
        """)

        conn.commit()
        print("Database tables created successfully")

    except Exception as e:
        print("Error creating tables:", e)

    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    # Get the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Change to that directory
    os.chdir(script_dir)
    create_tables()
