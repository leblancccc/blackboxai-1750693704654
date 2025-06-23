from libs.booking_libs import BookingLibs
from dbms.connection import Connect
import sys

def insert_booking(bookingInfo):
    conn=None
    sql="""INSERT INTO booking VALUES (?,?,?,?,?,?,?,?)"""
    values=(bookingInfo.getBookingid(), bookingInfo.getPickupaddress(), bookingInfo.getDate(),
            bookingInfo.getTime(), bookingInfo.getDropoffaddress(), bookingInfo.getBookingstatus(),
            bookingInfo.getCid(), bookingInfo.getDid())
    insertResult=False

    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        insertResult=True

    except:
        print("Error",sys.exc_info())

    finally:
        del values, sql, conn
        return insertResult


def update_booking(bookingInfo):
    conn=None
    sql="""UPDATE booking SET pickupaddress=?, date=?, time=?, dropoffaddress=?, bookingstatus=?,cid=?, did=? WHERE bookingid=?"""
    values=(bookingInfo.getPickupaddress(),
            bookingInfo.getDate(),
            bookingInfo.getTime(),
            bookingInfo.getDropoffaddress(),
            bookingInfo.getBookingstatus(),
            bookingInfo.getCid(),
            bookingInfo.getDid(),
            bookingInfo.getBookingid()
            )
    updatebookingResult=False
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        updatebookingResult=True

    except:
        print("Error", sys.exc_info())

    finally:
        del values, sql, conn
        return updatebookingResult

#
def select_all():
    conn=None
    sql="""SELECT * FROM booking WHERE bookingstatus='Pending'"""
    Bookresult=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        Bookresult=cursor.fetchall()
        cursor.close()
        conn.close()


    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return Bookresult


def total_booking():
    conn=None
    sql="""SELECT count(bookingid) from booking"""
    bookingResult=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        bookingResult=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return bookingResult

def customerbooking_selectall(cid):
    conn=None
    sql="""SELECT * FROM booking WHERE cid=?"""
    values=(cid,)
    Bookresult=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        Bookresult=cursor.fetchall()
        cursor.close()
        conn.close()


    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return Bookresult


def driver_update_booking(bookingInfo):
    conn=None
    sql="""UPDATE booking SET bookingstatus=? WHERE bookingid=?"""
    values=(bookingInfo.getBookingstatus(),bookingInfo.getBookingid())
    updatebookingResult=False
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        updatebookingResult=True

    except:
        print("Error", sys.exc_info())

    finally:
        del values, sql, conn
        return updatebookingResult

def customerbooking_selectstatsubooked(cid):
    conn=None
    sql="""SELECT * FROM booking WHERE cid=? and bookingstatus='Pending'"""
    values=(cid,)
    Bookresult=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        Bookresult=cursor.fetchall()
        cursor.close()
        conn.close()


    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return Bookresult

def update_customer_booking1(bookingInfo):
    conn=None
    sql="""UPDATE booking SET pickupaddress=?, date=?, time=?, dropoffaddress=? WHERE bookingid=?"""
    values=(bookingInfo.getPickupaddress(),
            bookingInfo.getDate(),
            bookingInfo.getTime(),
            bookingInfo.getDropoffaddress(),
            bookingInfo.getBookingid()
            )
    updatebookingResult=False
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        updatebookingResult=True

    except:
        print("Error", sys.exc_info())

    finally:
        del values, sql, conn
        return updatebookingResult


def delete_booking(bookingID):
    conn=None
    sql="""DELETE FROM booking WHERE bookingid=?"""
    values=(bookingID,)
    Deleteresult=False
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        Deleteresult=True


    except:
        print("Error", sys.exc_info())

    finally:
        del values, sql,conn
        return Deleteresult

def customer_checkbooking(cidInfo):
    conn=None
    sql="""select date from booking where cid=? and date=? and bookingstatus='Pending'"""
    values=(cidInfo.getCid(),cidInfo.getDate())
    checkResult=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        checkResult=cursor.fetchone()

    except:
        print("Error", sys.exc_info())

    finally:
        del values, sql, conn
        return checkResult


def active_booking12():
    conn=None
    sql="""select booking.bookingid, customers.name, booking.pickupaddress, 
    booking.dropoffaddress, booking.date, booking.time,drivers.name, booking.bookingstatus
     from booking inner join customers on booking.cid=customers.cid inner join drivers 
     on booking.did=drivers.did where booking.bookingstatus='Booked'"""
    activeResult=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        activeResult=cursor.fetchall()

    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return activeResult


def total_revenue():
    conn=None
    sql="""SELECT SUM(total) from billing"""
    totalResult=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        totalResult=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return totalResult


def validateadminbooking():
    conn=None
    sql="""select date from booking where bookingstatus='Pending'"""
    validateresult=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        validateresult=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return validateresult


def update_booking11(bid):
    conn=None
    sql="""UPDATE booking SET bookingstatus='Cancel' WHERE bookingid=?"""
    values=(bid,)
    updatebookingResult=False
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        updatebookingResult=True

    except:
        print("Error", sys.exc_info())

    finally:
        del values, sql, conn
        return updatebookingResult
